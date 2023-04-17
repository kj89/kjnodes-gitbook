# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/ojo.png" width="150" alt=""><figcaption></figcaption></figure>

Ojo is a decentralized security-first oracle network built  to support the Cosmos Ecosystem. Ojo will source price data  from a diverse catalog of on and off-chain sources and use  advanced security mechanisms to guarantee the integrity of the data it provides.

**Chain ID**: ojo-devnet | **Latest Version Tag**: v0.1.2 | **Wasm**: OFF

[Website](https://ojo.network) | [Discord](https://discord.gg/fd8Yrex8nC) | [Twitter](https://twitter.com/ojo_network)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/ojo-testnet](https://explorer.kjnodes.com/ojo-testnet)

## Public endpoints

* api: [https://ojo-testnet.api.kjnodes.com](https://ojo-testnet.api.kjnodes.com)
* rpc: [https://ojo-testnet.rpc.kjnodes.com](https://ojo-testnet.rpc.kjnodes.com)
* grpc: ojo-testnet.grpc.kjnodes.com:50090

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

**live-peers** (29)
```bash
peers="2c40b0aedc41b7c1b20c7c243dd5edd698428c41@138.201.85.176:26696,46be755bb7f34a6f4722713e40c9786266654396@38.242.237.125:26656,34a4c8433adfc4bf0df7c085ce58ed48664fbdc1@85.10.193.246:31656,c735f993287716ca1c358e9fe104dc570cf2ef3c@176.37.119.156:26694,f474a520009496972515f843cdb835fc7d663779@65.109.23.114:21656,50ad0e558d9da6fce98ae4527cd49ee3e8d19940@94.250.202.215:26656,f3e3a1d7684f3af1d434596e9b70ab21f4d67838@165.232.119.140:26656,34d194b6dab0159471a2aa318949f6a4a238d1b8@77.51.200.79:50656,3c6384ae2a167912a5ace2f5f8e38afc559715f0@75.119.156.88:26656,0ac9841750afe017b882768b0e29e72b8296d6b0@104.194.8.68:46656,d2489830a5e91ec214edfc54756512e4f89f2609@65.109.92.79:12656,cf2de6fcee7dd1e7bbe3413e9c182481f49eede0@65.108.9.164:21656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,446bf9b0ef6ea1b50c682f4f3427f46b9a70d5b3@65.109.116.204:21656,39e879a31a54215882647fb7299464036e322f50@65.109.65.163:21656,58f192f7c6aebe881f54bd133e9b8abf82bc3b20@65.108.13.154:36656,69ffa3745aa4ff20756fe66153619a52f348d1ef@139.59.142.164:50656,a1a6edee9e7928c97d8f99805757c09a1248b942@194.195.87.28:34656,7186f24ace7f4f2606f56f750c2684d387dc39ac@65.108.231.124:12656,bd90b71f1f982ebb18857da8cb777883d6ca687e@185.209.223.68:26656,66b140833cba7cadd92d544088d735e219adbf01@65.108.226.183:21656,69774d64905bb33ea805228ac875835aea09f25a@185.217.198.141:26656,9ea0473b3684dbf1f2cf194f69f746566dab6760@78.46.99.50:22656,d0973fcf352a68fda91624f05b7d90e171cce032@65.109.28.226:05656,e052b7c899bae41f6d89f70f81de50e28b72a7bf@38.242.237.100:26656,4e38368e64b1951439e7d6ac3387dae9dcfef120@94.130.16.254:60956,f63f353c1e8b47b6fe1cbbda91b5a91673c155b3@89.163.132.156:36656,b133dde2713a216a017399920419fcb1e084cdb2@136.243.88.91:7330,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
