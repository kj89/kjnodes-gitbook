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
peers="b4c7205397045d22fe762c8d2021fa4ce6d7ea1e@162.55.39.159:36656,239caa37cb0f131b01be8151631b649dc700cd97@95.217.200.36:46656,899892b43b951a5bb03cb2054e4d84f6431249cc@212.227.160.56:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,46be755bb7f34a6f4722713e40c9786266654396@38.242.237.125:26656,446bf9b0ef6ea1b50c682f4f3427f46b9a70d5b3@65.109.116.204:21656,98981d7eef057a01274473363addb7f0b17e06fa@84.21.171.25:26656,cf2de6fcee7dd1e7bbe3413e9c182481f49eede0@65.108.9.164:21656,c735f993287716ca1c358e9fe104dc570cf2ef3c@176.37.119.156:26694,d2489830a5e91ec214edfc54756512e4f89f2609@65.109.92.79:12656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,39e879a31a54215882647fb7299464036e322f50@65.109.65.163:21656,34a4c8433adfc4bf0df7c085ce58ed48664fbdc1@85.10.193.246:31656,66b140833cba7cadd92d544088d735e219adbf01@65.108.226.183:21656,7186f24ace7f4f2606f56f750c2684d387dc39ac@65.108.231.124:12656,c0ee71c74858b339787320596b805ed631c48ebb@213.133.100.172:27433,81d09ca7ba8f30812402f9076aad78e47f0afc7a@184.174.37.152:50656,b133dde2713a216a017399920419fcb1e084cdb2@136.243.88.91:7330,33d16e5cfd73bd8b600da03a0ac93f2a38691315@77.54.1.75:1202,11bb322f6396a1ca67717cf162385ed250503e28@154.12.253.123:36656,f702b19a4dae5ad813dabe3f529bf31c160a74e0@5.189.176.202:36656,4e38368e64b1951439e7d6ac3387dae9dcfef120@94.130.16.254:60956,c2f1a2474219cdd314e271429b415732261ebaa3@148.251.19.197:26666,41d974f9a97209a401546a61ea2638a0f8071d79@178.18.252.10:26656,855fc154f9054ce4055719e09ce6f7f1d0ecd9fb@85.10.198.171:36656,57847cb629cd707515b838a5baaf2b5c3ca0b022@65.108.199.206:37656,4640b6c775c05b6146a708a3b5ec2241c1688588@161.97.147.255:50656,d18abe07d27a732e913a782d31b691087a76078d@88.99.164.158:37096,bd90b71f1f982ebb18857da8cb777883d6ca687e@185.209.223.68:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
