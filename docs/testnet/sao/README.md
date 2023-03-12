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

**live-peers** (27)
```bash
peers="f4ebd48ae8b347eb71c43596f8c3b406807170ae@159.223.40.81:24556,2f5b05d5a8fe73c7dd2830c5face9c1b5316cdc8@65.21.131.215:15756,923df3e7e591a5716d51809e9366483fd3926a38@5.188.118.105:36656,e926078d739912b6c843503c13168dee2af6a207@45.14.194.30:26656,b417aa497b83a616ef77774773c3071fc216aad0@206.189.59.199:26656,3c769db2e0332c1728b87173084cdc9dc1ab24b2@65.21.134.202:15756,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:49656,bcb3f05e4b63a0e8dc5c57870e0412169d3a2290@109.123.243.68:26656,bf34e92211b840f044f8aed66455a73f9c7a4e10@167.99.73.24:26656,c5cad37c5b221088a78a3d5bd66e8db4b2672a30@144.126.148.198:26656,51064e987ab1193713957b6e07a70589d97d2903@157.245.197.58:26656,1d4c2290729dad5a5cb464b487e2922b88e0d4e0@65.109.117.23:49656,651a0314b0563c187691a4ff7e715b8dfb32eaa6@64.226.71.203:26656,a8dc98984aff5131b04afb408ac605fabfc5bfe4@64.226.72.32:26656,536ed23e7e75b3173da835995eec36be4b25dbc3@194.233.73.34:49656,f64f50dd41caf5f05ee1d567ead0a46feb4dec50@164.92.173.124:26656,cbe9fa91d3a603ca64c4eb22cca7f7fb18e0ff01@65.109.89.5:39656,04f9bad9b3b5c657dc7c11b341074028fb2faf2c@203.23.128.181:26656,91b67dd0d2904d95748e1ec5311e39033cfeaabc@65.109.92.240:1076,0c77942550c78ae8939b691b725a9dd7ffa4d864@185.219.142.182:27656,627d0c6e30676a0b4bdb73a324b1eb3a08e5cc45@137.184.197.65:26656,c6d7c5c8d8b780756f9ff31ef735221c4a589220@31.220.72.135:26656,0f73577b17dbf79f4d7d9d8486684357477cd400@143.198.136.136:26656,f551a6996b82111fcd050493cc360b3e4eb6d23c@143.198.198.2:49656,6a23f4da326ceeab0a6e112c25ff39715439b8ce@167.86.75.138:49656,3535b3f6181b8ba413cd9391515b9840aafc4b2a@142.132.194.157:26256,006e207a3f235a28bc0815001b76ee385ee4bda3@88.99.164.158:1076"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.sao/config/config.toml
```
