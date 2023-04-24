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

**live-peers** (27)
```bash
peers="b133dde2713a216a017399920419fcb1e084cdb2@136.243.88.91:7330,23830179727e6e38933e95000cb84ece4112f78c@185.155.97.74:18656,f63f353c1e8b47b6fe1cbbda91b5a91673c155b3@89.163.132.156:36656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,446bf9b0ef6ea1b50c682f4f3427f46b9a70d5b3@65.109.116.204:21656,cbe534c7d012e9eb4e71a5573aee8acc1adf4bc6@65.108.41.172:28056,39e879a31a54215882647fb7299464036e322f50@65.109.65.163:21656,c735f993287716ca1c358e9fe104dc570cf2ef3c@176.37.119.156:26694,cf2de6fcee7dd1e7bbe3413e9c182481f49eede0@65.108.9.164:21656,b6c75d1fbdc9c39daaaf52a4c0937b9f06975808@167.235.198.193:46656,f8a62360e6084b6a9ba3f731a1fb708ef3c9c5cf@143.198.136.136:28656,2905d22a658a7138c03c0259fba4c168260682bb@159.69.208.78:26656,d1c5c6bf4641d1800e931af6858275f08c20706d@23.88.5.169:18656,8e69c82fd42041a5eff49bcb94ae65c037aa45a9@65.109.87.88:26156,98981d7eef057a01274473363addb7f0b17e06fa@84.21.171.25:26656,5461b1ff958615ab65b97a788774c557921e72ec@89.117.57.201:19656,d2489830a5e91ec214edfc54756512e4f89f2609@65.109.92.79:12656,3cd8b55fbb2c4e87ee5e39554155051d0d98edc4@188.34.187.252:50656,9ea0473b3684dbf1f2cf194f69f746566dab6760@78.46.99.50:22656,11bb322f6396a1ca67717cf162385ed250503e28@154.12.253.123:36656,91eba8f362b6c41d324ff26f316ce0b50d22b955@213.136.84.176:10656,33d16e5cfd73bd8b600da03a0ac93f2a38691315@77.54.1.75:1202,41d974f9a97209a401546a61ea2638a0f8071d79@178.18.252.10:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,e3d56e1538e41115bccdcb0b83a734407d59d2b9@185.219.142.216:50656,a876f7cda5f1ddd16aa271ec43cba750c0ba32c4@77.37.176.99:26656,f12af93f4f59534a022192408c31fdd1d2f1bb0c@38.242.131.92:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
