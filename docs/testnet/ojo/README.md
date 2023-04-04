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

**live-peers** (40)
```bash
peers="c2f1a2474219cdd314e271429b415732261ebaa3@148.251.19.197:26666,17a0ee209f3deef0f88e1f1f296f05157340b594@5.75.254.44:50656,5a36595613f189a3c1096729897fb02be0a8c15e@89.117.50.187:28656,ae3621c022cddc8c05d7640c14147d257746fb74@185.215.166.73:26656,91eba8f362b6c41d324ff26f316ce0b50d22b955@213.136.84.176:10656,f4538b599f92e695b26409c0bd7da7e3b32eec4d@95.216.114.212:30656,0621bb73d18724cae4eb411e6b96765f95a3345e@178.63.8.245:61356,1786d7d18b39d5824cae23e8085c87883ed661e6@65.109.147.57:36656,577606f2072f97a5107bead5b2321302092c1f7d@194.5.152.12:26656,d9df87e2e26db62ef4014ce6e8705ee11bda304f@176.124.220.21:4669,e7aefcb24cfe3e6e27147b4202a6188a1bb76f2d@15.235.10.78:26656,5a53ebe6e029f8a26b1bc6dd8fe9a8efd57202f6@167.71.194.75:28656,cf2de6fcee7dd1e7bbe3413e9c182481f49eede0@65.108.9.164:21656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,f3e3a1d7684f3af1d434596e9b70ab21f4d67838@165.232.119.140:26656,da369d44c00dba309237b21391806504353d188f@194.163.187.175:50656,9d6ff8ca3c73ab08b7fcd59f47ed9cf7bd80f14e@185.217.126.187:36656,3fd91ce7928545f56eb9fbd61ebc355ade39021a@15.235.143.226:50656,239caa37cb0f131b01be8151631b649dc700cd97@95.217.200.36:46656,87cec7782444e2863f57c94b66c058f3533ffd60@158.220.106.208:26656,d30444b8fc8ae5867cd620651fdef2a064fded2a@89.64.74.222:26656,4609153f2b095b6c7f98b9cd3d079fe8fcd992db@95.216.14.58:61356,11bb322f6396a1ca67717cf162385ed250503e28@154.12.253.123:36656,f702b19a4dae5ad813dabe3f529bf31c160a74e0@5.189.176.202:26656,b6c75d1fbdc9c39daaaf52a4c0937b9f06975808@167.235.198.193:46656,affee2f485ca15c68c302ad98e8de41fcd0e71ba@162.19.238.49:26656,0ea23938eaefffe447eb0126d4951e2ac9c45637@45.140.147.252:26656,408ee86160af26ee7204d220498e80638f7874f4@161.97.109.47:38656,6fe7a28edc1ebe68d66223fdb09a9f7ea46a942d@74.208.253.159:10656,66b140833cba7cadd92d544088d735e219adbf01@65.108.226.183:21656,69774d64905bb33ea805228ac875835aea09f25a@185.217.198.141:26656,7186f24ace7f4f2606f56f750c2684d387dc39ac@65.108.231.124:12656,dd100ed6f1046f8db6d1d7ad04ed6253f935e9b2@176.118.198.128:26656,5461b1ff958615ab65b97a788774c557921e72ec@89.117.57.201:19656,f63f353c1e8b47b6fe1cbbda91b5a91673c155b3@89.163.132.156:36656,544540bc2fd9f9d003bc2a04923d7d346a1d9eaa@190.15.196.193:50656,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:21656,2086389fe8bb43133205d1a76792b5e58bc9f811@65.108.197.164:64646,899892b43b951a5bb03cb2054e4d84f6431249cc@212.227.160.56:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
