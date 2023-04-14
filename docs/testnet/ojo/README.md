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
peers="2c40b0aedc41b7c1b20c7c243dd5edd698428c41@138.201.85.176:26696,cf2de6fcee7dd1e7bbe3413e9c182481f49eede0@65.108.9.164:21656,9a60cf2bb51eed575d58170fcc55901fb99b40a0@194.163.148.202:50656,98981d7eef057a01274473363addb7f0b17e06fa@84.21.171.25:26656,c735f993287716ca1c358e9fe104dc570cf2ef3c@176.37.119.156:26694,9ea0473b3684dbf1f2cf194f69f746566dab6760@78.46.99.50:22656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,978cf9aca38f819fd8189272379fc3c2ae2682a8@213.239.218.210:56656,315350f9d96426d4a025dbdecae84ceca64d1638@95.217.40.230:56656,0d4dc8d9e80df99fdf7fbb0e44fbe55e0f8dde28@65.108.205.47:14756,eddfe8bf3c478fdd0281808371f9d9d1a3d63308@157.90.208.222:60956,2f739fc450015f90acc7f7199e77780d07616257@65.109.90.171:36656,b133dde2713a216a017399920419fcb1e084cdb2@136.243.88.91:7330,69774d64905bb33ea805228ac875835aea09f25a@185.217.198.141:26656,11bb322f6396a1ca67717cf162385ed250503e28@154.12.253.123:36656,7186f24ace7f4f2606f56f750c2684d387dc39ac@65.108.231.124:12656,7416a65de3cc548a537dbb8bdf93dbd83fe401d2@78.107.234.44:26656,50e9bd8647571268df2313df6c46ba9960c9f40e@178.128.88.30:26656,41d974f9a97209a401546a61ea2638a0f8071d79@178.18.252.10:26656,f63f353c1e8b47b6fe1cbbda91b5a91673c155b3@89.163.132.156:36656,ae3621c022cddc8c05d7640c14147d257746fb74@185.215.166.73:26656,a23cc4cbb09108bc9af380083108262454539aeb@35.215.116.65:26656,66b140833cba7cadd92d544088d735e219adbf01@65.108.226.183:21656,fee808fc235e2f345caaaee1d65f818d710f6433@213.137.237.201:26656,f3e3a1d7684f3af1d434596e9b70ab21f4d67838@165.232.119.140:26656,bef511f2c5244e6603bd74295e2dffb126d04f41@158.101.208.86:26656,b314955720069e8c98acf1cf1e896b68a3e306f9@65.108.4.161:27656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
