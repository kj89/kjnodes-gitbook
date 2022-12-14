# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/gitopia.png" width="150" alt=""><figcaption></figcaption></figure>

Gitopia is the next-generation Code Collaboration Platform fuelled by  a decentralized network and interactive token economy. It is designed  to optimize the open-source software development process through  collaboration, transparency, and incentivization.

**Chain ID**: gitopia-janus-testnet-2 | **Latest Version Tag**: v1.2.0 | **Wasm**: OFF

Website: [https://gitopia.com/](https://gitopia.com/)


## Public endpoints

* rpc: [https://gitopia-testnet.rpc.kjnodes.com](https://gitopia-testnet.rpc.kjnodes.com)
* api: [https://gitopia-testnet.api.kjnodes.com](https://gitopia-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@gitopia-testnet.rpc.kjnodes.com:41656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@gitopia-testnet.rpc.kjnodes.com:41659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/gitopia-testnet/addrbook.json > $HOME/.gitopia/config/addrbook.json
```

**live-peers** (35)
```
peers="1989ced6b71ce676a5ab4d0586d85e38fd41fbd2@136.243.88.91:7070,8f4c2887e46edc200a95afeaa87cb63bdddd26e2@185.239.208.131:656,5c2c2b27e1824097d4f5dc7a581a8d615923e76f@185.252.235.110:41656,95fbdc6d62be17db6688222b15b57d3e795ed07a@167.86.84.102:656,67e839cff368a20c9b7a1390b739d3538866b0b6@65.21.134.202:26356,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,66f94651fb02f277c90c605a38df549d3c0a9269@75.119.151.217:26656,8e9c65f65157cd5540e94335ae068c4040cf9b3b@83.171.249.165:656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,3b7845f8c8361c2f2de742473cd891c6e8cdeabf@83.171.249.159:656,09538ba6159f454a17d76501c59e23bad6fc9d3d@85.190.246.67:26656,023c6a86fbd8b8368503c92bd612a8c0379a26e5@194.146.13.251:656,37c3d29df83da59e5a258d413e2f89365ab05711@85.239.243.12:656,e79532749fb5dd95366f4568a7b2430d0e316fb5@84.46.255.163:26656,d159db085278927848c98b185b5871bf265669d9@185.250.36.169:41656,ff4fab3a07cdf3601b90ececd2de9a85b3a1a42e@82.208.21.152:26656,44a66336b029ba931165da3580cc6322af90339d@38.242.207.87:26656,b30d41820868f19784589dce150f07e3bdce8ea2@86.48.0.95:26656,f1c042fca05e4bfb9a6da1cccaa5108a26ea1e0f@65.108.104.167:28656,0d4c392f44c081347775643d99311bf2b36a7377@80.241.220.27:60956,599bb15403aae7679ba59f878ee8b9c39264fc93@185.213.25.129:60956,c03e9f152bb1becc54d4424d02249135d39be09f@81.0.218.106:41656,f4a2a6b840d1bad6f09c726d51f81d03f41c9ecc@194.146.13.246:656,b6651c7b043ef4bdccd7906b0f06de2bbdfe8a60@193.46.243.75:26656,32254e5e11c49d8802f4c5bbd2c682eebd72ea33@80.241.220.28:60956,e88708f6bda2af195f0ec48b9868e588ead964fb@144.91.82.239:26656,98bdfc67810bf7ac8f5c45b2c677b4bf199eb42e@185.193.67.65:41656,730983044bcc3f8e688bc2436da8a171fd843922@154.12.243.189:656,2f58a44c9ce9dcdf81e2eaed7cd808ebefe222a7@38.242.243.111:26656,0c37cd47e46901caadd8288a158edb81d37427a0@209.126.6.101:26656,481189b7e246f6c824a969482446c49abbfe76b8@161.97.172.147:26656,91bf3eb973595dd4621ccf5853e5ac78c48058da@194.163.180.77:656,b44d4fd0799d2c06fbec0257b376c0520bdb226a@185.250.37.147:41656,231ded997a112e8778afed3fd07ed7b98e0686e0@167.86.91.80:26656,d7f23c752c5790b9647e961277a4767f1ba33f20@95.216.168.99:36656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
