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

**live-peers** (24)
```bash
peers="622e5b7bc26be4edc4a9112ed0c5c8b00aa72721@185.246.84.196:26656,4cb932af43e2c64a0277516d96410a05294653de@75.119.148.69:26656,46984fe69d730d18bfc561830b729fb7689aea2b@95.216.14.46:22656,b6c75d1fbdc9c39daaaf52a4c0937b9f06975808@167.235.198.193:46656,39e879a31a54215882647fb7299464036e322f50@65.109.65.163:21656,c735f993287716ca1c358e9fe104dc570cf2ef3c@176.37.119.156:26694,446bf9b0ef6ea1b50c682f4f3427f46b9a70d5b3@65.109.116.204:21656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,0a54815282d06cd10ce30b5ba3f9721c6ca1b600@135.181.33.42:50656,eddfe8bf3c478fdd0281808371f9d9d1a3d63308@157.90.208.222:60956,f63f353c1e8b47b6fe1cbbda91b5a91673c155b3@89.163.132.156:36656,ed12aee3273baaaf01e357574c1692f12776446d@65.109.117.165:50656,41d974f9a97209a401546a61ea2638a0f8071d79@178.18.252.10:26656,5acc5ccc09dc10f5bc12c4ba4468a03c3df9d1ea@65.108.8.28:61356,d2489830a5e91ec214edfc54756512e4f89f2609@65.109.92.79:12656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,cabd6a59d90f477a4dd04e87543d01f97b9b619e@185.9.144.138:46656,d18abe07d27a732e913a782d31b691087a76078d@88.99.164.158:37096,a876f7cda5f1ddd16aa271ec43cba750c0ba32c4@77.37.176.99:26656,11bb322f6396a1ca67717cf162385ed250503e28@154.12.253.123:36656,9ea0473b3684dbf1f2cf194f69f746566dab6760@78.46.99.50:22656,fee808fc235e2f345caaaee1d65f818d710f6433@213.137.237.201:26656,f12af93f4f59534a022192408c31fdd1d2f1bb0c@38.242.131.92:26656,bd90b71f1f982ebb18857da8cb777883d6ca687e@185.209.223.68:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
