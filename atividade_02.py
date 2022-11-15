# from __future__ import print_function  # efetuando as mudanças.
# # Import MNIST data
#
# # from tensorflow.examples.tutorials.mnist import input_data
#
# import tensorflow_datasets
#
# mnist = tensorflow_datasets.load('mnist')
# # mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)
#
# import tensorflow.compat.v1 as tf
# tf.disable_v2_behavior()
#
# import matplotlib.pyplot as plt



from __future__ import print_function  # efetuando as mudanças.
# Import MNIST data
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)

import tensorflow as tf
import matplotlib.pyplot as plt

# Parametros
learning_rate = 0.001
training_epochs = 15
batch_size = 100
display_step = 1

# Parâmetros da Rede
n_hidden_1 = 256  # 1st layer number of features
n_hidden_2 = 256  # 2nd layer number of features
n_input = 784  # MNIST data input (img shape: 28*28)
n_classes = 10  # MNIST total classes (0-9 digits)

# entrando com o tf Graph
x = tf.placeholder("float", [None, n_input])
y = tf.placeholder("float", [None, n_classes])


# Criação do modelo
def multilayer_perceptron(x, weights, biases):
    # Hidden layer with RELU activation
    layer_1 = tf.add(tf.matmul(x, weights['h1']), biases['b1'])
    layer_1 = tf.nn.relu(layer_1)
    # Hidden layer with RELU activation
    layer_2 = tf.add(tf.matmul(layer_1, weights['h2']), biases['b2'])
    layer_2 = tf.nn.relu(layer_2)
    # Output layer with linear activation
    out_layer = tf.matmul(layer_2, weights['out']) + biases['out']
    return out_layer


# estabelecendo camadas, os pesos eo bias(layers weight & bias)
weights = {
    'h1': tf.Variable(tf.random_normal([n_input, n_hidden_1])),
    'h2': tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2])),
    'out': tf.Variable(tf.random_normal([n_hidden_2, n_classes]))
}

biases = {
    'b1': tf.Variable(tf.random_normal([n_hidden_1])),
    'b2': tf.Variable(tf.random_normal([n_hidden_2])),
    'out': tf.Variable(tf.random_normal([n_classes]))
}

# Construindo o modelo
pred = multilayer_perceptron(x, weights, biases)

# Definindo a perda e a otimizador
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred, labels=y))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

# Iniciando as variáveis
init = tf.global_variables_initializer()

# create an empty list to store the cost history and accuracy history
cost_history = []
accuracy_history = []

# Criando os graficos
with tf.Session() as sess:
    sess.run(init)

    # treinamento dos ciclos(épocas) de execução
    for epoch in range(training_epochs):
        avg_cost = 0.
        total_batch = int(mnist.train.num_examples / batch_size)
        # Loop over all batches
        for i in range(total_batch):
            batch_x, batch_y = mnist.train.next_batch(batch_size)

            # executando a otimização op (backprop) e custo de op (para valores perdidos)
            _, c = sess.run([optimizer, cost], feed_dict={x: batch_x, y: batch_y})
            # calculando a perda média
            avg_cost += c / total_batch
        # Display logs per epoch step
        if epoch % display_step == 0:
            correct_prediction = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
            # cálculo da acurária
            accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
            acu_temp = accuracy.eval({x: mnist.test.images, y: mnist.test.labels})
            # Adicionando a lista de acurária
            accuracy_history.append(acu_temp)
            # Adicionando o custo histórico
            cost_history.append(avg_cost)
            print("Epoch:", '%04d' % (epoch + 1), "- cost=", "{:.9f}".format(avg_cost), "- Accuracy=", acu_temp)

    print("Optimization Finished!")
    # plot the cost history
    plt.plot(cost_history)
    plt.show()
    # plot the accuracy history
    plt.plot(accuracy_history)
    plt.show()
    # Teste do modelo
    correct_prediction = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
    # Cálculo da acuracia
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
    print("Accuracy:", accuracy.eval({x: mnist.test.images, y: mnist.test.labels}))