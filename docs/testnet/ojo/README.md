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

**live-peers** (41)
```bash
peers="ac5089a8789736e2bc3eee0bf79ca04e22202bef@162.55.80.116:29656,2c40b0aedc41b7c1b20c7c243dd5edd698428c41@138.201.85.176:26696,ffe2d5ecb614762d5a1723f5f8b00d3feb6eb091@5.9.13.234:26686,3de750927e66b01bb566c1c189beeb43b7cde73f@213.239.216.252:47656,0ccc4bd8386fbec1421e3c19c24124eeb00b3293@46.101.144.90:28656,3c6384ae2a167912a5ace2f5f8e38afc559715f0@75.119.156.88:26656,8fbfa810cb666ddef1c9f4405e933ef49138f35a@65.108.199.120:54656,567b2c55ec74f07ed24a3f286922b199d62f3d8c@81.0.219.36:36656,a3a9014f82cb69fe0494ea3bc49990027d081a5a@65.108.126.35:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,1145755896d6a3e9df2f130cc2cbd223cdb206f0@209.145.53.163:29656,f35a6ea4693d24d3727a8e866acab2a9faa2ddbc@91.223.3.144:26256,1e2a49792b0e0686827ec0fbc101a9ad709e0f28@88.210.9.78:26656,d5b2ae8815b09a30ab253957f7eca052dde3101d@65.108.9.164:24656,f474a520009496972515f843cdb835fc7d663779@65.109.23.114:21656,7186f24ace7f4f2606f56f750c2684d387dc39ac@65.108.231.124:12656,b133dde2713a216a017399920419fcb1e084cdb2@136.243.88.91:7330,8f414276a2cb7a97d37a3e126c186972e1968039@65.108.4.233:56656,bf834f428aed19dd1937d66327cb6244d7722b0d@65.108.201.189:26676,2691bb6b296b951400d871c8d0bd94a3a1cdbd52@65.109.93.152:33656,108037355c949c6fb4d7618f5ae04cbdc66c3362@65.108.206.96:27656,b16d876c443850cd358596790411b835d3f1735b@95.214.53.46:35656,11bb322f6396a1ca67717cf162385ed250503e28@154.12.253.123:36656,b6b4a4c720c4b4a191f0c5583cc298b545c330df@65.109.28.219:21656,c2ed1269cd275202e4d69fdb64e194e59b20f573@185.245.182.152:40656,d2beb0153f6ee3d2a5a90f96848c71bff2b25eb0@65.109.90.171:36656,7416a65de3cc548a537dbb8bdf93dbd83fe401d2@78.107.234.44:26656,725988cccb088855f4fd5a1548aaa08b7bafec96@65.108.43.58:27675,4764a447ea3518e5017756b42ca5f6442b2f5768@5.161.114.1:26656,323d4309091003ea96ec3076b8bf4dc319c71345@109.205.182.137:26656,f4663c5df8ee2e2b6e1cc6a9d7ad09687a27e08c@68.183.32.158:26656,a23cc4cbb09108bc9af380083108262454539aeb@35.215.116.65:26656,3832f6d02addadfe4acfbd1a87ccc009642a348e@195.46.165.3:26656,cb706ebe1d7a1f1d3e281bf46a78d84251f50810@95.216.14.72:26656,67e95aeec46d7c5840f9685ca2b4cd725841b814@16.163.74.176:26636,cabd6a59d90f477a4dd04e87543d01f97b9b619e@185.9.144.138:46656,67a1f07c7743d9bec92e11faad5bffe9bc08a178@130.185.119.243:50656,bef511f2c5244e6603bd74295e2dffb126d04f41@158.101.208.86:26656,ca46b2279f09daf8e89a8571ad1ccb3f8e6d0463@185.15.244.245:50656,2cd65afacab69b6ebfa4f9a8435f5f7df5fbb735@135.181.160.61:32656,3c8b9cf60b33bdd8b41db6d8af1009e91e14afc8@5.78.67.243:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
