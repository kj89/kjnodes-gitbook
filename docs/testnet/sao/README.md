# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/sao.png" width="150" alt=""><figcaption></figcaption></figure>

SAO Network is a secure and decentralized Web3 storage infrastructure  based on Cosmos SDK and IPFS protocol. It aims to facilitate the adoption  of Web3 storage, support the growing demand for Web3 applications and  allow for a more decentralized way of storing and accessing data.

**Chain ID**: sao-testnet0 | **Latest Version Tag**: v0.0.9 | **Wasm**: OFF

[Website](https://www.sao.network) | [Discord](https://discord.gg/f4xzfvPhhA) | [Twitter](https://twitter.com/SAONetwork)




## Chain explorer
[https://explorer.kjnodes.com/sao-testnet](https://explorer.kjnodes.com/sao-testnet)

## Public endpoints

* api: [https://sao-testnet.api.kjnodes.com](https://sao-testnet.api.kjnodes.com)
* rpc: [https://sao-testnet.rpc.kjnodes.com](https://sao-testnet.rpc.kjnodes.com)
* grpc: [https://sao-testnet.grpc.kjnodes.com](https://sao-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@sao-testnet.rpc.kjnodes.com:49656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@sao-testnet.rpc.kjnodes.com:49659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/sao-testnet/addrbook.json > $HOME/.sao/config/addrbook.json
```

**live-peers** (30)
```bash
peers="7075469d8ed68a423e065b67bcde29b6ca4266fd@142.132.248.253:65528,70502c3cbd5aabc12245f44bebf767d83fe76434@134.209.255.7:20656,266d8a31a1cecf8d2f673e4cb65ea736173428e9@165.22.76.250:20656,0a661ed79b169c7c2b0f289c436e35900bb0de90@157.97.108.38:24556,658f473c2399f87c5e5ff4d329c8c53ae9f399e0@46.101.232.154:26656,6a23f4da326ceeab0a6e112c25ff39715439b8ce@167.86.75.138:49656,ada0a0b4b5b3d290cae51b946b33a1079d00df72@185.197.250.35:27656,ec7e0b075202f836feac71f017a90e0d83674cb8@65.108.9.164:24556,a76917f23b26c7c4918104d0e06a24c28f9077bd@5.161.50.28:26656,8c6201e793348d8f89dedcae6df3cd36198477fd@94.46.187.220:26656,72a2bbeb32621600de4b2a6ed42b11bf3be1105c@146.190.40.115:20656,8167fbcc27bbf431f36b9a980c7ec57803502f2e@206.189.81.5:20656,a22a3ad8f847ab87bd64d0b9365b870750bde4e5@143.198.204.248:20656,0c77942550c78ae8939b691b725a9dd7ffa4d864@185.219.142.182:27656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:49656,91b67dd0d2904d95748e1ec5311e39033cfeaabc@65.109.92.240:1076,e81848f87aea44ec6fc53155a0818165ed4ce6f3@164.92.80.34:24556,557c49ddc6c98e5c5ac6030a93451ad5fcd54e34@164.90.147.133:20656,1b6164aab8350eeb71bd46ebfe641e5d103a3f8e@143.244.132.66:26656,a9112494955b579ab18671281da88dd3f3f6cbca@139.59.170.199:26656,0c78af85c2fb11a4c5b09f357595bd671438e6eb@172.105.127.215:26656,aa269fc09dc0b73e45f1c6b514aea634fa0193c7@45.88.223.247:27656,cec1fdc272372d8254aaa33dcf12016c6ad1dbf6@65.109.24.121:26656,5ad9a3d2ccc5faeb55285c7fd4edc1f3c6eeb8b8@137.184.116.168:26656,2794f6fa1ffc87bee2e644dd6f77b2bda33fa4be@206.81.13.193:49656,5cea6b9e5a2ffd5f42a42515fefdd44a7631d048@101.80.228.209:26656,5f0fd4bae47a933f2b87eb52f4f093a95cbd7dd3@195.201.83.242:18656,0b477f865e2f3212bf911a6e9a15d333c9033fa9@38.242.229.239:26656,b9bec1902b4817dc07952078512fdb8fe0306bc4@89.58.45.204:60656,e711b6631c3e5bb2f6c389cbc5d422912b05316b@213.239.216.252:41256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.sao/config/config.toml
```
