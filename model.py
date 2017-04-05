import numpy as np
import tensorflow as tf

LABELS = {
    'Alternative': 0,
    'Blues': 1,
    'Classical': 2,
    'Country': 3,
    'D&B': 4,
    'Disco': 5,
    'Dubstep': 6,
    'Electronic': 7,
    'Folk': 8,
    'Funk': 9,
    'Hip-Hop': 10,
    'House': 11,
    'Indie': 12,
    'Jazz': 13,
    'Metal': 14,
    'Pop': 15,
    'Punk': 16,
    'R&B': 17,
    'Rap': 18,
    'Reggaeton': 19,
    'Reggae': 20,
    'Rock': 21,
    'Salsa': 22,
    'Ska': 23,
    'Soul': 24,
    'Trance': 25
}

a = [0.060044332071022014, 0.09256943722585365, 3.229191199592342, 0.10333672684937564, 0.10680541710498384, 0.6483497954845685, 0.0005339389443620013, 0.10906379440665155, -18.053733382048748, 1.0529201257111402, 0.4706549668444886, 0.09186266923535122, 0.04118372956108708, 0.2982920572447628, 0.08941394289766233, 0.23340801315769788, 0.1452328742085503, 0.23646803108256953, 0.08467395797738746, 0.13989504522056445, 0.011480950638394178, 0.0008241214750160425, 0.00032531156149942807, 0.0013970597339743925, 0.0038200281865720643, 0.0012260947639084058, 0.002062501062159956, 0.0006276509205219237, 0.0009378335002593735, 0.0014572569986470954, 0.002335818327519821, 0.0009543639595907601, 0.0005801856114991682, 0.002130862728855644, 0.011310256302907334, 0.034843814116956265, 0.11709644458083954, 0.01193211624486746, 0.015279145735162005, 0.14234646528306558, 0.00090869373302776, 0.021107197478106264, 2.326548578826517, 0.37546014970601677, 0.333555025141662, 0.2062417192528601, 0.1559255403703218, 0.15472051833458828, 0.16460034314376287, 0.16737063699536983, 0.15699352196145555, 0.12910339623595132, 0.16755117137789638, 0.163328925577391, 0.15590259041911592, 0.0013856241222374413, 0.0002391165649511032, 0.0015151595177747006, 0.007029753687924601, 0.0011533236333034688, 0.0022116872003646315, 0.0005393961784410449, 0.0008400521497526614, 0.0013855367852901289, 0.007564802096299622, 0.0016304873269209152, 0.0007990716287605345, 0.0037493521818732986, 150.0]

b = [0.028668688727673662, 0.010296874642310268, 2.979289570795993, 0.07771797022261993, 0.12198492962551129, 0.07406470247848689, 0.001981627735053664, 0.039223117818555996, -23.012398288066628, 2.450383013402157, -0.7209535825894928, 0.07425339479431828, -0.47001386542844525, 0.006088903086235553, 0.01620690020921406, 0.21418823151639632, -0.052091687642100086, -0.014820133215621163, -0.04205860250594405, 0.04366025985499307, -0.031519931259828125, 0.002860475089759992, 0.0003646468375155665, 0.002032433781725561, 0.0021552882054243646, 0.0025839743774277875, 0.0009058216527170049, 0.0008695032351243258, 0.00068567444148368, 0.0006254911744017183, 0.0007357199054872923, 0.0006408451163334997, 0.002221595279796925, 0.0020110988491125782, 0.006846064570096212, 0.008456917276021512, 0.34895182207509867, 0.06382364407926983, 0.0707189929354555, 0.06751763540513239, 0.0010086845302658034, 0.014315807864655895, 4.4706546531721365, 0.43612756476174575, 0.40739917406157244, 0.35130193768906803, 0.2341932299542251, 0.1972104508417759, 0.23544222276288154, 0.1671490418787359, 0.3489483337061661, 0.2637239292016653, 0.23975431205775216, 0.21894401585821305, 0.2024376957834217, 0.006628432758045184, 0.00038632059557007806, 0.005343911639298718, 0.002902033201242365, 0.00517548217374744, 0.002131617367862237, 0.0012211411343064536, 0.0009310703900695344, 0.0005492201558132859, 0.0007178880923363045, 0.0007566149509813329, 0.006080275164001775, 0.0026897796057824743, 199.99999999999997]

c = [0.13169837562454179, 0.03747907258948448, 3.2093567363765194, 0.20415217142414294, 0.1783023422538795, 1.2981390056554678, 0.00013002260238153973, 0.24316704459561597, -18.057689533187364, 1.0821583049391887, 0.022808529642138784, 0.1549138769242293, 0.5485543540631203, 0.24687343351752963, 0.001938394071525701, -0.029246965650714545, 0.32433651932613095, 0.5493794894195386, -0.1532108536935117, -0.15953240858525616, -0.14292504685871826, 0.001022193915855823, 0.000574248578652918, 0.003744947243702289, 0.0006085355445014114, 0.002063131254826033, 0.003100602255608477, 0.0014455207769336613, 0.003737979544046202, 0.0006869733130853256, 0.0018058484190229462, 0.0019889269642760373, 0.0013000858126485423, 0.0019709657966293925, 0.018371489884997885, 0.0038319853094609868, 0.053279939984258194, 0.012001309617731878, 0.007287461986689352, 0.1875974718744425, 4.252950874934398e-05, 0.04607723005339392, 0.2630779792539925, 0.23210117834659488, 0.17928284477236567, 0.12835441277409773, 0.3027672361440782, 0.12774041196099692, 0.14183339098145453, 0.23304445814417998, 0.2613883636021474, 0.212724386971971, 0.1524114531785372, 0.15298324799066315, 0.11769770369920446, 0.0010044220119722683, 0.00047814477640875284, 0.003668243077559693, 0.0003353471455472499, 0.0022506117030398343, 0.003720407974634264, 0.0010744772528963858, 0.003050953233744261, 0.0005532878059932616, 0.0015633060547211519, 0.001632379520800961, 0.0009701856688470633, 0.0010768320828846707, 199.99999999999997]

load = np.loadtxt("test.txt")
print (load)
na = np.array(load)
na_ = np.array([c])
labels = np.array([[0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                    [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]])

labels_ = np.array([[0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]])

x = tf.placeholder(tf.float32, [None, 69]) #[num_images, dimensionality of each]
W = tf.Variable(tf.zeros([69, 26])) #[dimensionality of input, dimensionality of output]
b = tf.Variable(tf.zeros([26])) #[dimensionality of output]
y = tf.matmul(x, W) + b #the model, will have dimensionality num_images, num_outputs

y_ = tf.placeholder(tf.float32, [None, 26])

  #loss function
cross_entropy = tf.reduce_mean(
  tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))

  #training step with learning rate
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

    #create session
sess = tf.InteractiveSession()

    #initialize variables
tf.global_variables_initializer().run()


for _ in range(1000):
    # batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: na, y_: labels})

correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print(sess.run(accuracy, feed_dict={x: na_,
                                    y_: labels_}))
