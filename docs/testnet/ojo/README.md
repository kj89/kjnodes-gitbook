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

**live-peers** (25)
```bash
peers="fee808fc235e2f345caaaee1d65f818d710f6433@213.137.237.201:26656,d2489830a5e91ec214edfc54756512e4f89f2609@65.109.92.79:12656,39e879a31a54215882647fb7299464036e322f50@65.109.65.163:21656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,90823c2a23f30ea161ca5ad4d34bbcc8f98c86e5@89.117.55.108:28656,446bf9b0ef6ea1b50c682f4f3427f46b9a70d5b3@65.109.116.204:21656,c735f993287716ca1c358e9fe104dc570cf2ef3c@176.37.119.156:26694,cf2de6fcee7dd1e7bbe3413e9c182481f49eede0@65.108.9.164:21656,a876f7cda5f1ddd16aa271ec43cba750c0ba32c4@77.37.176.99:26656,91eba8f362b6c41d324ff26f316ce0b50d22b955@213.136.84.176:10656,9fa6a54e5b9207ea53ddd123f7b417e864b5769d@65.108.49.114:26656,2905d22a658a7138c03c0259fba4c168260682bb@159.69.208.78:26656,b6c75d1fbdc9c39daaaf52a4c0937b9f06975808@167.235.198.193:46656,ae3621c022cddc8c05d7640c14147d257746fb74@185.215.166.73:26656,20d9bb13b09c054c30f1b48fbd276aa255af5a34@65.108.238.147:37656,11bb322f6396a1ca67717cf162385ed250503e28@154.12.253.123:36656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,4ffdad68a6c6302168e0951766ffa1921c9b19a4@199.175.98.136:26656,0c89a312b6fc88661ff78642eb04defd29bd7e9c@65.108.98.124:60466,b133dde2713a216a017399920419fcb1e084cdb2@136.243.88.91:7330,5461b1ff958615ab65b97a788774c557921e72ec@89.117.57.201:19656,dd100ed6f1046f8db6d1d7ad04ed6253f935e9b2@176.118.198.128:26656,f63f353c1e8b47b6fe1cbbda91b5a91673c155b3@89.163.132.156:36656,577606f2072f97a5107bead5b2321302092c1f7d@194.5.152.12:26656,bd90b71f1f982ebb18857da8cb777883d6ca687e@185.209.223.68:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
