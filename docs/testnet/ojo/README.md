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
peers="2905d22a658a7138c03c0259fba4c168260682bb@159.69.208.78:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,0c89a312b6fc88661ff78642eb04defd29bd7e9c@65.108.98.124:60466,239caa37cb0f131b01be8151631b649dc700cd97@95.217.200.36:46656,98981d7eef057a01274473363addb7f0b17e06fa@84.21.171.25:26656,ae3621c022cddc8c05d7640c14147d257746fb74@185.215.166.73:26656,da369d44c00dba309237b21391806504353d188f@194.163.187.175:50656,d2489830a5e91ec214edfc54756512e4f89f2609@65.109.92.79:12656,c735f993287716ca1c358e9fe104dc570cf2ef3c@176.37.119.156:26694,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,39e879a31a54215882647fb7299464036e322f50@65.109.65.163:21656,446bf9b0ef6ea1b50c682f4f3427f46b9a70d5b3@65.109.116.204:21656,cf2de6fcee7dd1e7bbe3413e9c182481f49eede0@65.108.9.164:21656,46be755bb7f34a6f4722713e40c9786266654396@38.242.237.125:26656,a876f7cda5f1ddd16aa271ec43cba750c0ba32c4@77.37.176.99:26656,41d974f9a97209a401546a61ea2638a0f8071d79@178.18.252.10:26656,c2f1a2474219cdd314e271429b415732261ebaa3@148.251.19.197:26666,9bcec17faba1b8f6583d37103f20bd9b968ac857@38.146.3.230:21656,0a54815282d06cd10ce30b5ba3f9721c6ca1b600@135.181.33.42:50656,1b81440d84a2746af6fba80c1a3a091f298f7a7a@185.206.214.254:26656,11bb322f6396a1ca67717cf162385ed250503e28@154.12.253.123:36656,5461b1ff958615ab65b97a788774c557921e72ec@89.117.57.201:19656,ed367ee00b2155c743be6f5b635de6e7ea5acc64@149.202.73.104:11356,b133dde2713a216a017399920419fcb1e084cdb2@136.243.88.91:7330,dd100ed6f1046f8db6d1d7ad04ed6253f935e9b2@176.118.198.128:26656,f63f353c1e8b47b6fe1cbbda91b5a91673c155b3@89.163.132.156:36656,66b140833cba7cadd92d544088d735e219adbf01@65.108.226.183:21656,371f313df7f79b34d65f026769a3e0c3e77127eb@45.137.67.238:26656,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
