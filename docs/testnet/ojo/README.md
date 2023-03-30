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
peers="2c40b0aedc41b7c1b20c7c243dd5edd698428c41@138.201.85.176:26696,affee2f485ca15c68c302ad98e8de41fcd0e71ba@162.19.238.49:26656,e6b70cf272ec33d3915a94c60b68637935643fd3@194.163.167.138:59656,2f739fc450015f90acc7f7199e77780d07616257@65.109.90.171:36656,371f313df7f79b34d65f026769a3e0c3e77127eb@45.137.67.238:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,fee808fc235e2f345caaaee1d65f818d710f6433@213.137.237.201:26656,11bb322f6396a1ca67717cf162385ed250503e28@154.12.253.123:36656,f3e3a1d7684f3af1d434596e9b70ab21f4d67838@165.232.119.140:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,d5b2ae8815b09a30ab253957f7eca052dde3101d@65.108.9.164:24656,bab2e24e088af1efc88684a83024fa31baad34e5@185.137.122.106:26656,0ea23938eaefffe447eb0126d4951e2ac9c45637@45.140.147.252:26656,b6c75d1fbdc9c39daaaf52a4c0937b9f06975808@167.235.198.193:46656,5af3d50dcc231884f3d3da3e3caecb0deef1dc5b@142.132.134.112:25356,4609153f2b095b6c7f98b9cd3d079fe8fcd992db@95.216.14.58:61356,174e741215a8957222d8be785072dd81b1634ec7@178.159.5.176:51656,239caa37cb0f131b01be8151631b649dc700cd97@95.217.200.36:46656,da369d44c00dba309237b21391806504353d188f@194.163.187.175:50656,0621bb73d18724cae4eb411e6b96765f95a3345e@178.63.8.245:61356,7186f24ace7f4f2606f56f750c2684d387dc39ac@65.108.231.124:12656,50ad0e558d9da6fce98ae4527cd49ee3e8d19940@94.250.202.215:26656,f474a520009496972515f843cdb835fc7d663779@65.109.23.114:21656,5d9be9cf3d5161e4891b96a956c3c83de6c0ae49@5.78.75.124:26656,8036aed2d37890ddf245e7288b4fc724a301d728@65.109.117.23:50656,0ac9841750afe017b882768b0e29e72b8296d6b0@104.194.8.68:46656,ed12aee3273baaaf01e357574c1692f12776446d@65.109.117.165:50656,e29f2c959a5b21d994f09facf40afed417ed7984@154.26.155.102:36656,9ea0473b3684dbf1f2cf194f69f746566dab6760@78.46.99.50:22656,3c6384ae2a167912a5ace2f5f8e38afc559715f0@75.119.156.88:26656,47d4244f367fd3e14f25f73a6c3ac1f74ee81ef8@109.110.63.147:26656,8e69c82fd42041a5eff49bcb94ae65c037aa45a9@65.109.87.88:26156,b6b4a4c720c4b4a191f0c5583cc298b545c330df@65.109.28.219:21656,5264a9742c3e2fdb3803ff4af0ecb6e127c73ab1@135.181.16.252:27656,9d6ff8ca3c73ab08b7fcd59f47ed9cf7bd80f14e@185.217.126.187:36656,7416a65de3cc548a537dbb8bdf93dbd83fe401d2@78.107.234.44:26656,408ee86160af26ee7204d220498e80638f7874f4@161.97.109.47:38656,57847cb629cd707515b838a5baaf2b5c3ca0b022@65.108.199.206:37656,f63f353c1e8b47b6fe1cbbda91b5a91673c155b3@89.163.132.156:36656,2086389fe8bb43133205d1a76792b5e58bc9f811@65.108.197.164:64646"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
