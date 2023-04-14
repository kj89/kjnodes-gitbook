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
peers="34a4c8433adfc4bf0df7c085ce58ed48664fbdc1@85.10.193.246:31656,0ccc4bd8386fbec1421e3c19c24124eeb00b3293@46.101.144.90:28656,eddfe8bf3c478fdd0281808371f9d9d1a3d63308@157.90.208.222:60956,2f739fc450015f90acc7f7199e77780d07616257@65.109.90.171:36656,f474a520009496972515f843cdb835fc7d663779@65.109.23.114:21656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,bab2e24e088af1efc88684a83024fa31baad34e5@185.137.122.106:26656,c735f993287716ca1c358e9fe104dc570cf2ef3c@176.37.119.156:26694,cf2de6fcee7dd1e7bbe3413e9c182481f49eede0@65.108.9.164:21656,a23cc4cbb09108bc9af380083108262454539aeb@35.215.116.65:26656,0ae4649c788cd2e86fc1ee0a45dc245c6716004e@95.214.55.25:35656,fee808fc235e2f345caaaee1d65f818d710f6433@213.137.237.201:26656,81d09ca7ba8f30812402f9076aad78e47f0afc7a@184.174.37.152:50656,f6d6e625759814e157457a5889961e02dba26ba6@65.109.92.240:37096,4bfc6d62d115a2440f9e5dc10c21d302dbdf5c64@34.220.136.165:26656,fe8c46222c3a013115797176623597aafc16e33a@173.212.203.238:46656,9ea0473b3684dbf1f2cf194f69f746566dab6760@78.46.99.50:22656,b133dde2713a216a017399920419fcb1e084cdb2@136.243.88.91:7330,11bb322f6396a1ca67717cf162385ed250503e28@154.12.253.123:36656,7416a65de3cc548a537dbb8bdf93dbd83fe401d2@78.107.234.44:26656,bfdeba21ca39394ab264fff9c16188b6ecdace6d@144.91.82.61:26656,46be755bb7f34a6f4722713e40c9786266654396@38.242.237.125:26656,9ebe723eef929e9eff748f4046d6130ee349a398@65.108.203.149:24017,23830179727e6e38933e95000cb84ece4112f78c@185.155.97.74:18656,7186f24ace7f4f2606f56f750c2684d387dc39ac@65.108.231.124:12656,66b140833cba7cadd92d544088d735e219adbf01@65.108.226.183:21656,d18abe07d27a732e913a782d31b691087a76078d@88.99.164.158:37096,98981d7eef057a01274473363addb7f0b17e06fa@84.21.171.25:26656,f63f353c1e8b47b6fe1cbbda91b5a91673c155b3@89.163.132.156:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
