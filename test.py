
# controller = Controller("COM7")
# controller.start()
 
# message1 = DiscoveryRequest()
# promise1 = controller.send(message1).then(on_ready, on_error)
 
# message2 = RequestNodeInfoRequest(1)
# promise2 = controller.send(message1).then(on_ready, on_error)
 
# Promise.wait_all(promise1, promise2)

import promise from Promise.py

print("Start a promise")