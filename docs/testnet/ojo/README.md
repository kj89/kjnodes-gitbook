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

**live-peers** (23)
```bash
peers="5af3d50dcc231884f3d3da3e3caecb0deef1dc5b@142.132.134.112:25356,c0ee71c74858b339787320596b805ed631c48ebb@213.133.100.172:27433,affee2f485ca15c68c302ad98e8de41fcd0e71ba@162.19.238.49:26656,fbeb2b37fe139399d7513219e25afd9eb8f81f4f@65.21.170.3:38656,dc19e5d986ea79e70180cfbee7789de9cd79e14e@95.217.57.232:56656,97ff540b57b89dd0b6737eddb92977523dd5a7b3@195.3.221.58:12656,8a8b9a8a58c922a7693715100710697ec69b1478@65.109.92.235:11086,7416a65de3cc548a537dbb8bdf93dbd83fe401d2@78.107.234.44:26656,8671c2dbbfd918374292e2c760704414d853f5b7@35.215.121.109:26656,b0968b57bcb5e527230ef3cfa3f65d5f1e4647dd@35.212.224.95:26656,a23cc4cbb09108bc9af380083108262454539aeb@35.215.116.65:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,d5b2ae8815b09a30ab253957f7eca052dde3101d@65.108.9.164:24656,2223f5bf494729b9e9fdf6693d116d34e9d29755@141.94.193.28:55756,567b2c55ec74f07ed24a3f286922b199d62f3d8c@81.0.219.36:36656,239caa37cb0f131b01be8151631b649dc700cd97@95.217.200.36:46656,f474a520009496972515f843cdb835fc7d663779@65.109.23.114:21656,6f304029cb1b7fbcbe1359d57cbb69ae8dbcccfc@207.180.243.64:36656,b6b4a4c720c4b4a191f0c5583cc298b545c330df@65.109.28.219:21656,2c40b0aedc41b7c1b20c7c243dd5edd698428c41@138.201.85.176:26696,9bcec17faba1b8f6583d37103f20bd9b968ac857@38.146.3.230:21656,7186f24ace7f4f2606f56f750c2684d387dc39ac@65.108.231.124:12656,3a2c9a7631c26006a5d1943c004ab2da8c04d7b7@5.161.201.79:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
