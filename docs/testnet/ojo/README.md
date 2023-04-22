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

**live-peers** (28)
```bash
peers="66b140833cba7cadd92d544088d735e219adbf01@65.108.226.183:21656,3c6384ae2a167912a5ace2f5f8e38afc559715f0@75.119.156.88:26656,39e879a31a54215882647fb7299464036e322f50@65.109.65.163:21656,d2489830a5e91ec214edfc54756512e4f89f2609@65.109.92.79:12656,b33500a3aaeb7fa116bdbddbe9c91c3158f38f8d@128.199.18.172:26656,cf2de6fcee7dd1e7bbe3413e9c182481f49eede0@65.108.9.164:21656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,da9e028814ff30ec24e94bec6887f4686f692b86@173.212.222.167:30656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,c735f993287716ca1c358e9fe104dc570cf2ef3c@176.37.119.156:26694,446bf9b0ef6ea1b50c682f4f3427f46b9a70d5b3@65.109.116.204:21656,124439d1c16b1ee7ca1a39961f02fadf8539cb81@38.102.85.10:26656,a654bbc2b27134da4eb1fcc08f07a2c9ea0deec7@51.79.77.103:12656,7186f24ace7f4f2606f56f750c2684d387dc39ac@65.108.231.124:12656,98981d7eef057a01274473363addb7f0b17e06fa@84.21.171.25:26656,4e38368e64b1951439e7d6ac3387dae9dcfef120@94.130.16.254:60956,b133dde2713a216a017399920419fcb1e084cdb2@136.243.88.91:7330,0d4dc8d9e80df99fdf7fbb0e44fbe55e0f8dde28@65.108.205.47:14756,41d974f9a97209a401546a61ea2638a0f8071d79@178.18.252.10:26656,fee808fc235e2f345caaaee1d65f818d710f6433@213.137.237.201:26656,2155de2f62e75c9a5b0c013c756420dd23f59914@142.132.209.236:21656,11bb322f6396a1ca67717cf162385ed250503e28@154.12.253.123:36656,cbe534c7d012e9eb4e71a5573aee8acc1adf4bc6@65.108.41.172:28056,8e69c82fd42041a5eff49bcb94ae65c037aa45a9@65.109.87.88:26156,f63f353c1e8b47b6fe1cbbda91b5a91673c155b3@89.163.132.156:36656,bfdeba21ca39394ab264fff9c16188b6ecdace6d@144.91.82.61:26656,e8484ecab4b95e96cb5bffbd71aeae4808582e69@194.34.232.150:50656,46be755bb7f34a6f4722713e40c9786266654396@38.242.237.125:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
