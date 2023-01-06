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
peers="4432d927cd43ac192701830bed2ba589c6602a7e@165.227.148.44:26656,374da78901e59810277fc35482bce6e30953f488@80.79.6.155:41656,7f2339fc6a6dca666d8ffbbe4e61443d58e0e759@109.123.255.8:26656,fb0a1c5dbc329b1b0ae3dac6776df4eb5f2072f6@79.137.248.142:26656,a52d22191c38d7406f7b7bd8b3969f35d7c31c8b@146.190.62.4:26656,e8d068f922eaaf8784232198d701d39770f346cf@46.101.43.139:26656,e88708f6bda2af195f0ec48b9868e588ead964fb@144.91.82.239:26656,c15c3fee20da5db1e087066c8ff0b77457178f0d@65.108.217.101:26656,7182dfadba43a9a3b35f6862e63f75be20c8b1db@95.217.214.125:41656,996e783f3df1e83e0886eac6c7dc4af451e87fc5@95.165.89.222:24136,4ceba74efb843cf10926a9ec757e4e2081d71e92@207.244.226.183:656,2c000afaa7adeee6f9a34bba8fddd3a05b11922e@167.172.78.75:26656,f0b8227e40f25eaec0e25b9e91ca199d2d9a1ecb@167.86.94.177:656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,19fb417249992ae8def277fb753656da318fe250@38.242.133.239:41656,426863534b14513990b6b9dd2d8e085993c326d4@161.97.145.13:41656,b6651c7b043ef4bdccd7906b0f06de2bbdfe8a60@193.46.243.75:26656,eccdf1d5bf33bc1733838562b4d4a4a45869c3a8@135.181.183.93:41656,458a98d6293064bdf3d6f86e0e2aa87bbb450f07@75.119.144.48:656,8f4c2887e46edc200a95afeaa87cb63bdddd26e2@185.239.208.131:656,07272f3ff38780896f6d0f1c3a2ce1868fb0b968@173.249.49.120:36656,d3fe4d63101e72c4cc5fd1114b57d36b759c0402@164.92.72.200:26656,74a4bbfbf4d1ca9852d10f3a97e4d012c62aec9e@146.190.102.111:41656,292c099fc654a1331d3b62a1b939f867b62ef434@45.85.147.242:656,0c31077af45cb4f0424e58c91b0a917c36a90fd9@65.108.195.235:16656,5c58d5c43b0a93a28da0cd528af7921567a43921@146.190.34.12:41656,61d2b313e2adc9d7990944f8ab5a6f9ecf08084f@65.21.122.171:16656,dea00215e54c4098a4f194a7ecd43e24ea99336f@88.99.95.81:26656,1cf3826ccd9a24caa549cbea061446716858133e@154.26.130.95:36656,31099d763305ead833b84c28b142ecbfd3628a64@85.190.246.250:41656,407eb21b784f1dc4e9902cb812b65eec760c6a19@185.193.66.67:656,3989c44e8af3427b22a71a94185e85df99d450b4@149.102.158.188:41656,b44d4fd0799d2c06fbec0257b376c0520bdb226a@185.250.37.147:41656,ebeba690d8084592a983da1e6429598cc9b9d04c@213.202.212.77:26656,182a0faf787f0f62ac2af8975d951ab94573d7d2@194.195.87.52:41656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
