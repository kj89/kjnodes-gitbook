# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/ojo.png" alt=""><figcaption></figcaption></figure>

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
peers="9fa6a54e5b9207ea53ddd123f7b417e864b5769d@65.108.49.114:26656,9a60cf2bb51eed575d58170fcc55901fb99b40a0@194.163.148.202:50656,3c6384ae2a167912a5ace2f5f8e38afc559715f0@75.119.156.88:26656,50e9bd8647571268df2313df6c46ba9960c9f40e@178.128.88.30:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,cf2de6fcee7dd1e7bbe3413e9c182481f49eede0@65.108.9.164:21656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,d2489830a5e91ec214edfc54756512e4f89f2609@65.109.92.79:12656,446bf9b0ef6ea1b50c682f4f3427f46b9a70d5b3@65.109.116.204:21656,c735f993287716ca1c358e9fe104dc570cf2ef3c@176.37.119.156:26694,39e879a31a54215882647fb7299464036e322f50@65.109.65.163:21656,1761db35a0402af7d6008705a49dad5c9059ae63@195.231.38.226:28656,9d9d7a060cdf621b275c5127e736ad25f381eb6b@95.214.52.138:25676,c6125d3f9c979230b161216c4549f0f52679a645@54.38.193.93:26686,34a4c8433adfc4bf0df7c085ce58ed48664fbdc1@85.10.193.246:31656,a876f7cda5f1ddd16aa271ec43cba750c0ba32c4@77.37.176.99:26656,b6c75d1fbdc9c39daaaf52a4c0937b9f06975808@167.235.198.193:46656,2c40b0aedc41b7c1b20c7c243dd5edd698428c41@138.201.85.176:26696,4ffdad68a6c6302168e0951766ffa1921c9b19a4@199.175.98.136:26656,11bb322f6396a1ca67717cf162385ed250503e28@154.12.253.123:36656,dd100ed6f1046f8db6d1d7ad04ed6253f935e9b2@176.118.198.128:26656,b133dde2713a216a017399920419fcb1e084cdb2@136.243.88.91:7330,5461b1ff958615ab65b97a788774c557921e72ec@89.117.57.201:19656,0ae4649c788cd2e86fc1ee0a45dc245c6716004e@95.214.55.25:35656,f63f353c1e8b47b6fe1cbbda91b5a91673c155b3@89.163.132.156:36656,371f313df7f79b34d65f026769a3e0c3e77127eb@45.137.67.238:26656,057e1ebe8aed2c27bcacb0eeb54dee01f3c6eddd@65.108.200.49:8656,408ee86160af26ee7204d220498e80638f7874f4@161.97.109.47:38656,d18abe07d27a732e913a782d31b691087a76078d@88.99.164.158:37096,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
