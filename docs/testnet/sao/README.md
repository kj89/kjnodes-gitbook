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

**live-peers** (35)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:49656,f4ebd48ae8b347eb71c43596f8c3b406807170ae@159.223.40.81:24556,a8dc98984aff5131b04afb408ac605fabfc5bfe4@64.226.72.32:26656,0cd94d1d2808b009decbd9468b1f1b2cb3a0e0a6@171.250.164.181:49656,2f5b05d5a8fe73c7dd2830c5face9c1b5316cdc8@65.21.131.215:15756,e926078d739912b6c843503c13168dee2af6a207@45.14.194.30:26656,923df3e7e591a5716d51809e9366483fd3926a38@5.188.118.105:36656,51064e987ab1193713957b6e07a70589d97d2903@157.245.197.58:26656,0c77942550c78ae8939b691b725a9dd7ffa4d864@185.219.142.182:27656,bcb3f05e4b63a0e8dc5c57870e0412169d3a2290@109.123.243.68:26656,9248e2c9d075f095ea2ada4cd86294f946d8678e@149.102.129.76:26656,1d4c2290729dad5a5cb464b487e2922b88e0d4e0@65.109.117.23:49656,651a0314b0563c187691a4ff7e715b8dfb32eaa6@64.226.71.203:26656,5f0fd4bae47a933f2b87eb52f4f093a95cbd7dd3@195.201.83.242:18656,cbe9fa91d3a603ca64c4eb22cca7f7fb18e0ff01@65.109.89.5:39656,5ed578e78207183e46bb009e2ae79745981f46d8@165.22.52.163:26656,6642a126fbf5b2f8aa2f22dc169a9bb98f1c17a3@170.64.188.152:26656,be4d5db39afa804eb2eb9c44acecb43efd4527dc@65.109.81.119:21656,b9bec1902b4817dc07952078512fdb8fe0306bc4@89.58.45.204:60656,0f73577b17dbf79f4d7d9d8486684357477cd400@143.198.136.136:26656,91b67dd0d2904d95748e1ec5311e39033cfeaabc@65.109.92.240:1076,f551a6996b82111fcd050493cc360b3e4eb6d23c@143.198.198.2:49656,244c464e3d500ee3f242fa3a10ae50d4cd02fc26@164.90.221.101:26656,39320c6f494f7e091ce9b40e7ed49b1abb6b6c5d@95.217.57.232:46656,902240030667c196d2857dd43da27f0fa83b5225@170.64.172.224:26656,3c769db2e0332c1728b87173084cdc9dc1ab24b2@65.21.134.202:15756,536ed23e7e75b3173da835995eec36be4b25dbc3@194.233.73.34:49656,627d0c6e30676a0b4bdb73a324b1eb3a08e5cc45@137.184.197.65:26656,a22a3ad8f847ab87bd64d0b9365b870750bde4e5@143.198.204.248:20656,8028ba794ab03b98518cf0e3a76256dd4c82ff11@138.201.248.108:49656,5524049dff1e180a85adc2c9494f59c336e631fa@164.92.91.248:20656,c6d7c5c8d8b780756f9ff31ef735221c4a589220@31.220.72.135:26656,8631d6d74cf6ad0906ab3602606ad64ae920a9a9@174.138.22.160:26656,006e207a3f235a28bc0815001b76ee385ee4bda3@88.99.164.158:1076,063ddedc8c2498e94b337263e7b54187fa90bba1@118.68.153.14:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.sao/config/config.toml
```
