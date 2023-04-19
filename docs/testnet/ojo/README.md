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
peers="5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,2f739fc450015f90acc7f7199e77780d07616257@65.109.90.171:36656,fee808fc235e2f345caaaee1d65f818d710f6433@213.137.237.201:26656,4e38368e64b1951439e7d6ac3387dae9dcfef120@94.130.16.254:60956,c735f993287716ca1c358e9fe104dc570cf2ef3c@176.37.119.156:26694,11bb322f6396a1ca67717cf162385ed250503e28@154.12.253.123:36656,39e879a31a54215882647fb7299464036e322f50@65.109.65.163:21656,cf2de6fcee7dd1e7bbe3413e9c182481f49eede0@65.108.9.164:21656,d2489830a5e91ec214edfc54756512e4f89f2609@65.109.92.79:12656,446bf9b0ef6ea1b50c682f4f3427f46b9a70d5b3@65.109.116.204:21656,7186f24ace7f4f2606f56f750c2684d387dc39ac@65.108.231.124:12656,b6c75d1fbdc9c39daaaf52a4c0937b9f06975808@167.235.198.193:46656,5acc5ccc09dc10f5bc12c4ba4468a03c3df9d1ea@65.108.8.28:61356,b133dde2713a216a017399920419fcb1e084cdb2@136.243.88.91:7330,9a60cf2bb51eed575d58170fcc55901fb99b40a0@194.163.148.202:50656,0d4dc8d9e80df99fdf7fbb0e44fbe55e0f8dde28@65.108.205.47:14756,34a4c8433adfc4bf0df7c085ce58ed48664fbdc1@85.10.193.246:31656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,5a53ebe6e029f8a26b1bc6dd8fe9a8efd57202f6@167.71.194.75:28656,f63f353c1e8b47b6fe1cbbda91b5a91673c155b3@89.163.132.156:36656,ac5089a8789736e2bc3eee0bf79ca04e22202bef@162.55.80.116:29656,bd90b71f1f982ebb18857da8cb777883d6ca687e@185.209.223.68:26656,b33500a3aaeb7fa116bdbddbe9c91c3158f38f8d@128.199.18.172:26656,41d974f9a97209a401546a61ea2638a0f8071d79@178.18.252.10:26656,dd100ed6f1046f8db6d1d7ad04ed6253f935e9b2@176.118.198.128:26656,577606f2072f97a5107bead5b2321302092c1f7d@194.5.152.12:26656,a876f7cda5f1ddd16aa271ec43cba750c0ba32c4@77.37.176.99:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
