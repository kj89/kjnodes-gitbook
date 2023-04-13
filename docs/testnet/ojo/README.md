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

**live-peers** (30)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,cf2de6fcee7dd1e7bbe3413e9c182481f49eede0@65.108.9.164:21656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,a23cc4cbb09108bc9af380083108262454539aeb@35.215.116.65:26656,239caa37cb0f131b01be8151631b649dc700cd97@95.217.200.36:46656,46be755bb7f34a6f4722713e40c9786266654396@38.242.237.125:26656,25edf9d95199a89bb868d40a7bbeb0ca1f940a65@159.223.77.250:28656,57847cb629cd707515b838a5baaf2b5c3ca0b022@65.108.199.206:37656,0d4dc8d9e80df99fdf7fbb0e44fbe55e0f8dde28@65.108.205.47:14756,11bb322f6396a1ca67717cf162385ed250503e28@154.12.253.123:36656,5d9be9cf3d5161e4891b96a956c3c83de6c0ae49@5.78.75.124:26656,bab2e24e088af1efc88684a83024fa31baad34e5@185.137.122.106:26656,9ea0473b3684dbf1f2cf194f69f746566dab6760@78.46.99.50:22656,f63f353c1e8b47b6fe1cbbda91b5a91673c155b3@89.163.132.156:36656,66b140833cba7cadd92d544088d735e219adbf01@65.108.226.183:21656,2f739fc450015f90acc7f7199e77780d07616257@65.109.90.171:36656,f474a520009496972515f843cdb835fc7d663779@65.109.23.114:21656,7416a65de3cc548a537dbb8bdf93dbd83fe401d2@78.107.234.44:26656,a654bbc2b27134da4eb1fcc08f07a2c9ea0deec7@51.79.77.103:12656,cbe534c7d012e9eb4e71a5573aee8acc1adf4bc6@65.108.41.172:28056,eddfe8bf3c478fdd0281808371f9d9d1a3d63308@157.90.208.222:60956,b6c75d1fbdc9c39daaaf52a4c0937b9f06975808@167.235.198.193:46656,4e309b79b9147a0243f6e0cbc824f86e10bd09de@65.109.234.254:50656,b133dde2713a216a017399920419fcb1e084cdb2@136.243.88.91:7330,c735f993287716ca1c358e9fe104dc570cf2ef3c@176.37.119.156:26694,9bcec17faba1b8f6583d37103f20bd9b968ac857@38.146.3.230:21656,34a4c8433adfc4bf0df7c085ce58ed48664fbdc1@85.10.193.246:31656,fee808fc235e2f345caaaee1d65f818d710f6433@213.137.237.201:26656,98981d7eef057a01274473363addb7f0b17e06fa@84.21.171.25:26656,577606f2072f97a5107bead5b2321302092c1f7d@194.5.152.12:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
