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
peers="ac5089a8789736e2bc3eee0bf79ca04e22202bef@162.55.80.116:29656,8e69c82fd42041a5eff49bcb94ae65c037aa45a9@65.109.87.88:26156,5461b1ff958615ab65b97a788774c557921e72ec@89.117.57.201:19656,c735f993287716ca1c358e9fe104dc570cf2ef3c@176.37.119.156:26694,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,46be755bb7f34a6f4722713e40c9786266654396@38.242.237.125:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,d2489830a5e91ec214edfc54756512e4f89f2609@65.109.92.79:12656,b133dde2713a216a017399920419fcb1e084cdb2@136.243.88.91:7330,446bf9b0ef6ea1b50c682f4f3427f46b9a70d5b3@65.109.116.204:21656,39e879a31a54215882647fb7299464036e322f50@65.109.65.163:21656,cf2de6fcee7dd1e7bbe3413e9c182481f49eede0@65.108.9.164:21656,42baeb39425394727c10025ab26afb0b0e97a388@154.31.34.160:50656,4e38368e64b1951439e7d6ac3387dae9dcfef120@94.130.16.254:60956,9a60cf2bb51eed575d58170fcc55901fb99b40a0@194.163.148.202:50656,964adc99a6580ccf7fabbebfa42d3e1e70058ba0@85.190.254.15:50656,dd100ed6f1046f8db6d1d7ad04ed6253f935e9b2@176.118.198.128:26656,34d194b6dab0159471a2aa318949f6a4a238d1b8@77.51.200.79:50656,f8a62360e6084b6a9ba3f731a1fb708ef3c9c5cf@143.198.136.136:28656,33d16e5cfd73bd8b600da03a0ac93f2a38691315@77.54.1.75:1202,23830179727e6e38933e95000cb84ece4112f78c@185.155.97.74:18656,d18abe07d27a732e913a782d31b691087a76078d@88.99.164.158:37096,f35a6ea4693d24d3727a8e866acab2a9faa2ddbc@91.223.3.144:26256,b6c75d1fbdc9c39daaaf52a4c0937b9f06975808@167.235.198.193:46656,c2f1a2474219cdd314e271429b415732261ebaa3@148.251.19.197:26666,f63f353c1e8b47b6fe1cbbda91b5a91673c155b3@89.163.132.156:36656,11bb322f6396a1ca67717cf162385ed250503e28@154.12.253.123:36656,bd90b71f1f982ebb18857da8cb777883d6ca687e@185.209.223.68:26656,a876f7cda5f1ddd16aa271ec43cba750c0ba32c4@77.37.176.99:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
