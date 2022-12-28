# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/gitopia.png" width="150" alt=""><figcaption></figcaption></figure>

Gitopia is the next-generation Code Collaboration Platform fuelled by  a decentralized network and interactive token economy. It is designed  to optimize the open-source software development process through  collaboration, transparency, and incentivization.

**Chain ID**: gitopia-janus-testnet-2 | **Latest Version Tag**: v1.2.0 | **Wasm**: OFF

[Website](https://gitopia.com/) | [Discord](https://discord.gg/hFTXCGNYDZ) | [Twitter](https://twitter.com/gitopiaDAO)


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
peers="4977214dacb3713797653c1bc07b5982bcc91649@142.132.253.112:51656,3b7845f8c8361c2f2de742473cd891c6e8cdeabf@83.171.249.159:656,12f6b84a23b054a6591c647c2a4456c40af65cce@5.9.147.22:24656,7ff7410c2ef28adc5634e9bf7d313046e45f6089@206.81.21.146:26656,ccf24b1e4f8566f3914c08e13d2b6154ed47ddbd@45.153.48.45:26656,3bcba60fe08bb6ce59abc19b84cf58e7c915e0ed@193.46.243.243:656,374da78901e59810277fc35482bce6e30953f488@80.79.6.155:41656,fbe3b1e34e1dfe9ae2cd0db471b0a807bbb3c5f2@65.109.90.178:11356,c19da021d6bbdeccdd03453a021d7171e6e299d5@173.249.14.30:656,591318ade07c267271bb27790acec9e80dc1ce14@65.21.105.9:26656,4ceba74efb843cf10926a9ec757e4e2081d71e92@207.244.226.183:656,95fbdc6d62be17db6688222b15b57d3e795ed07a@167.86.84.102:656,fb0a1c5dbc329b1b0ae3dac6776df4eb5f2072f6@79.137.248.142:26656,f97115243c6291081b546e8d59f51e5ecede4168@149.102.155.225:26656,31099d763305ead833b84c28b142ecbfd3628a64@85.190.246.250:41656,d159db085278927848c98b185b5871bf265669d9@185.250.36.169:41656,bc8a2179df7d5db14504e64cfba8ad4e3d3ce0e4@38.242.156.105:26656,c6dcaf5c1d59c696a5b93f53cc5a855b2399f09c@149.102.146.49:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,8e9c65f65157cd5540e94335ae068c4040cf9b3b@83.171.249.165:656,4b74a2394e9c251ca24c68e666288a5fdae78010@185.245.183.246:26656,19fb417249992ae8def277fb753656da318fe250@38.242.133.239:41656,5fb72a0bea398ce56fa20cd732623f98d774be7d@149.102.128.208:41656,61c85d47e1dd86d5a5849450b849078d4d13184b@85.239.244.123:26656,2ef464f5acb300ed319f18fb082c7455a05e7cca@89.163.209.88:26656,02c20307295465ab2592fd81176e66be90d4bbe2@5.189.159.111:26656,ea53a3f77fe373f47be4e77fd5f9ff526dfaec33@51.79.143.46:41656,73de34b1d08fdd58b5a5c0ec6d2560310c1ebe90@38.242.151.86:26656,007d2419fea80aee707d009af0153f5105c53379@38.242.139.164:656,ebeba690d8084592a983da1e6429598cc9b9d04c@213.202.212.77:26656,f0b8227e40f25eaec0e25b9e91ca199d2d9a1ecb@167.86.94.177:656,72bac43328190fa83cbcb4e45abd9b96014122b8@164.92.255.96:26656,fea7c372588898f7ea3a04373c52a30712b3c279@185.239.209.56:656,1983d3cbcbc281232b5946ba9a2487e8f6976817@149.102.148.141:26656,8f4c2887e46edc200a95afeaa87cb63bdddd26e2@185.239.208.131:656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
