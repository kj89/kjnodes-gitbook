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
peers="2155de2f62e75c9a5b0c013c756420dd23f59914@142.132.209.236:21656,66b140833cba7cadd92d544088d735e219adbf01@65.108.226.183:21656,d6318facf0de085644dcf8ba57bcc1725b6ec515@89.58.59.75:36656,39e879a31a54215882647fb7299464036e322f50@65.109.65.163:21656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,c735f993287716ca1c358e9fe104dc570cf2ef3c@176.37.119.156:26694,50e9bd8647571268df2313df6c46ba9960c9f40e@178.128.88.30:26656,446bf9b0ef6ea1b50c682f4f3427f46b9a70d5b3@65.109.116.204:21656,cf2de6fcee7dd1e7bbe3413e9c182481f49eede0@65.108.9.164:21656,d2489830a5e91ec214edfc54756512e4f89f2609@65.109.92.79:12656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,b133dde2713a216a017399920419fcb1e084cdb2@136.243.88.91:7330,ed12aee3273baaaf01e357574c1692f12776446d@65.109.117.165:50656,e0fb84d102a7a43e13362c848df725d6868aed55@144.76.164.139:37656,23830179727e6e38933e95000cb84ece4112f78c@185.155.97.74:18656,f63f353c1e8b47b6fe1cbbda91b5a91673c155b3@89.163.132.156:36656,02cbe3e13614ae34d847fbab3a03567788e17b84@65.109.122.105:60956,fee808fc235e2f345caaaee1d65f818d710f6433@213.137.237.201:26656,11bb322f6396a1ca67717cf162385ed250503e28@154.12.253.123:36656,5461b1ff958615ab65b97a788774c557921e72ec@89.117.57.201:19656,b6c75d1fbdc9c39daaaf52a4c0937b9f06975808@167.235.198.193:46656,a876f7cda5f1ddd16aa271ec43cba750c0ba32c4@77.37.176.99:26656,98981d7eef057a01274473363addb7f0b17e06fa@84.21.171.25:26656,d0973fcf352a68fda91624f05b7d90e171cce032@65.109.28.226:05656,41d974f9a97209a401546a61ea2638a0f8071d79@178.18.252.10:26656,408ee86160af26ee7204d220498e80638f7874f4@161.97.109.47:38656,bfdeba21ca39394ab264fff9c16188b6ecdace6d@144.91.82.61:26656,bd90b71f1f982ebb18857da8cb777883d6ca687e@185.209.223.68:26656,dd100ed6f1046f8db6d1d7ad04ed6253f935e9b2@176.118.198.128:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
