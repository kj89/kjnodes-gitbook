# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/ojo.png" width="150" alt=""><figcaption></figcaption></figure>

Ojo is a decentralized security-first oracle network built  to support the Cosmos Ecosystem. Ojo will source price data  from a diverse catalog of on and off-chain sources and use  advanced security mechanisms to guarantee the integrity of the data it provides.

**Chain ID**: ojo-devnet | **Latest Version Tag**: v0.1.2 | **Wasm**: OFF

[Website](https://ojo.network) | [Discord](https://discord.gg/fd8Yrex8nC) | [Twitter](https://twitter.com/ojo_network)




## Chain explorer
[https://explorer.kjnodes.com/ojo-testnet](https://explorer.kjnodes.com/ojo-testnet)

## Public endpoints

* api: [https://ojo-testnet.api.kjnodes.com](https://ojo-testnet.api.kjnodes.com)
* rpc: [https://ojo-testnet.rpc.kjnodes.com](https://ojo-testnet.rpc.kjnodes.com)
* grpc: [https://ojo-testnet.grpc.kjnodes.com](https://ojo-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@ojo-testnet.rpc.kjnodes.com:50656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@ojo-testnet.rpc.kjnodes.com:50659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/ojo-testnet/addrbook.json > $HOME/.ojo/config/addrbook.json
```

**live-peers** (42)
```bash
peers="8e69c82fd42041a5eff49bcb94ae65c037aa45a9@65.109.87.88:26156,f70138a8bbca35814ed947184821f8a561651793@185.234.69.143:30656,50ad0e558d9da6fce98ae4527cd49ee3e8d19940@94.250.202.215:26656,8036aed2d37890ddf245e7288b4fc724a301d728@65.109.117.23:50656,97a388be825fc69fca40a8a3de75aa5794602abb@95.217.225.212:36656,a3a9014f82cb69fe0494ea3bc49990027d081a5a@65.108.126.35:36656,c37e444f67af17545393ad16930cd68dc7e3fd08@95.216.7.169:61156,f474a520009496972515f843cdb835fc7d663779@65.109.23.114:21656,cd4d7ffdad8bd258cd90c22ec7197c0fdf9f3648@38.242.134.73:27656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,0d4dc8d9e80df99fdf7fbb0e44fbe55e0f8dde28@65.108.205.47:14756,d2489830a5e91ec214edfc54756512e4f89f2609@65.109.92.79:12656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,9aeb9250f279c9e288b7db702380e2970a36e248@5.188.118.105:46656,4764a447ea3518e5017756b42ca5f6442b2f5768@5.161.114.1:26656,f4663c5df8ee2e2b6e1cc6a9d7ad09687a27e08c@68.183.32.158:26656,8671c2dbbfd918374292e2c760704414d853f5b7@35.215.121.109:26656,855fc154f9054ce4055719e09ce6f7f1d0ecd9fb@85.10.198.171:36656,a9bcb95ee047c4a909c675dc36c556eafe1248e1@195.201.174.109:46656,ca46b2279f09daf8e89a8571ad1ccb3f8e6d0463@185.15.244.245:50656,4609153f2b095b6c7f98b9cd3d079fe8fcd992db@95.216.14.58:61356,62fa77951a7c8f323c0499fff716cd86932d8996@65.108.199.36:24214,b6b4a4c720c4b4a191f0c5583cc298b545c330df@65.109.28.219:21656,b133dde2713a216a017399920419fcb1e084cdb2@136.243.88.91:7330,67a1f07c7743d9bec92e11faad5bffe9bc08a178@130.185.119.243:50656,0ac9841750afe017b882768b0e29e72b8296d6b0@104.194.8.68:46656,7416a65de3cc548a537dbb8bdf93dbd83fe401d2@78.107.234.44:26656,9ea0473b3684dbf1f2cf194f69f746566dab6760@78.46.99.50:22656,f702b19a4dae5ad813dabe3f529bf31c160a74e0@5.189.176.202:26656,f12af93f4f59534a022192408c31fdd1d2f1bb0c@38.242.131.92:26656,3ae9b1f545cb78a361971259cbeff41341fabb3c@65.108.97.58:2626,d9df87e2e26db62ef4014ce6e8705ee11bda304f@176.124.220.21:4669,d5b2ae8815b09a30ab253957f7eca052dde3101d@65.108.9.164:24656,7186f24ace7f4f2606f56f750c2684d387dc39ac@65.108.231.124:12656,a23cc4cbb09108bc9af380083108262454539aeb@35.215.116.65:26656,b0968b57bcb5e527230ef3cfa3f65d5f1e4647dd@35.212.224.95:26656,4bfc6d62d115a2440f9e5dc10c21d302dbdf5c64@34.220.136.165:26656,bab2e24e088af1efc88684a83024fa31baad34e5@185.137.122.106:26656,67c653cec3e0e116939841b9c601b43daecae47e@116.202.170.159:24656,d18abe07d27a732e913a782d31b691087a76078d@88.99.164.158:37096,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:21656,83c547ae2fb272ccec4ea7cc90376e293d8df112@138.201.203.134:35656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
