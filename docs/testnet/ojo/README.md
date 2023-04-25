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
peers="d1c5c6bf4641d1800e931af6858275f08c20706d@23.88.5.169:18656,9ebe723eef929e9eff748f4046d6130ee349a398@65.108.203.149:24017,46be755bb7f34a6f4722713e40c9786266654396@38.242.237.125:26656,50ad0e558d9da6fce98ae4527cd49ee3e8d19940@94.250.202.215:26656,c735f993287716ca1c358e9fe104dc570cf2ef3c@176.37.119.156:26694,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,446bf9b0ef6ea1b50c682f4f3427f46b9a70d5b3@65.109.116.204:21656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,030c769628e3e56928f8fd143ce9bd9ce53dba34@31.220.85.212:46656,39e879a31a54215882647fb7299464036e322f50@65.109.65.163:21656,cf2de6fcee7dd1e7bbe3413e9c182481f49eede0@65.108.9.164:21656,d2489830a5e91ec214edfc54756512e4f89f2609@65.109.92.79:12656,a876f7cda5f1ddd16aa271ec43cba750c0ba32c4@77.37.176.99:26656,174e741215a8957222d8be785072dd81b1634ec7@178.159.5.176:51656,f63f353c1e8b47b6fe1cbbda91b5a91673c155b3@89.163.132.156:36656,34a4c8433adfc4bf0df7c085ce58ed48664fbdc1@85.10.193.246:31656,4ffdad68a6c6302168e0951766ffa1921c9b19a4@199.175.98.136:26656,fee808fc235e2f345caaaee1d65f818d710f6433@213.137.237.201:26656,f616a5d02454f0d80460896a0b7d8dfba8bdbac9@173.249.21.248:26656,11bb322f6396a1ca67717cf162385ed250503e28@154.12.253.123:36656,9ea0473b3684dbf1f2cf194f69f746566dab6760@78.46.99.50:22656,0e5e110fc015fd3cdd4b465fbedf6218ffc5e9ee@65.108.78.101:50656,1879aa588b4d6431bf40543f3a44129dcf60a043@144.91.77.68:50656,b314955720069e8c98acf1cf1e896b68a3e306f9@65.108.4.161:27656,b6c75d1fbdc9c39daaaf52a4c0937b9f06975808@167.235.198.193:46656,b133dde2713a216a017399920419fcb1e084cdb2@136.243.88.91:7330,5461b1ff958615ab65b97a788774c557921e72ec@89.117.57.201:19656,bd90b71f1f982ebb18857da8cb777883d6ca687e@185.209.223.68:26656,15101a8cead0eadffc1b822f902bed71051e1638@5.166.240.95:26656,23da6727d574bd04ac40cc8c9cbe301ba8dbdc34@185.198.27.139:32656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
