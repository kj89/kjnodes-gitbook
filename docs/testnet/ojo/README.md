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
* grpc: ojo-testnet.grpc.kjnodes.com:15090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@ojo-testnet.rpc.kjnodes.com:15056
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@ojo-testnet.rpc.kjnodes.com:15059
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/ojo-testnet/addrbook.json > $HOME/.ojo/config/addrbook.json
```

**live-peers** (24)
```bash
peers="0a54815282d06cd10ce30b5ba3f9721c6ca1b600@135.181.33.42:50656,1761db35a0402af7d6008705a49dad5c9059ae63@195.231.38.226:28656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,c735f993287716ca1c358e9fe104dc570cf2ef3c@176.37.119.156:26694,446bf9b0ef6ea1b50c682f4f3427f46b9a70d5b3@65.109.116.204:21656,b314955720069e8c98acf1cf1e896b68a3e306f9@65.108.4.161:27656,39e879a31a54215882647fb7299464036e322f50@65.109.65.163:21656,d2489830a5e91ec214edfc54756512e4f89f2609@65.109.92.79:12656,2905d22a658a7138c03c0259fba4c168260682bb@159.69.208.78:26656,0d4dc8d9e80df99fdf7fbb0e44fbe55e0f8dde28@65.108.205.47:14756,f8a62360e6084b6a9ba3f731a1fb708ef3c9c5cf@143.198.136.136:28656,4ffdad68a6c6302168e0951766ffa1921c9b19a4@199.175.98.136:26656,f63f353c1e8b47b6fe1cbbda91b5a91673c155b3@89.163.132.156:36656,98981d7eef057a01274473363addb7f0b17e06fa@84.21.171.25:26656,41d974f9a97209a401546a61ea2638a0f8071d79@178.18.252.10:26656,a876f7cda5f1ddd16aa271ec43cba750c0ba32c4@77.37.176.99:26656,c6125d3f9c979230b161216c4549f0f52679a645@54.38.193.93:26686,b133dde2713a216a017399920419fcb1e084cdb2@136.243.88.91:7330,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,8671c2dbbfd918374292e2c760704414d853f5b7@35.215.121.109:26656,11bb322f6396a1ca67717cf162385ed250503e28@154.12.253.123:36656,f12af93f4f59534a022192408c31fdd1d2f1bb0c@38.242.131.92:26656,b5279c10108e5cab375df5d9adbfa18c7fccf7ec@158.220.106.208:26656,b6c75d1fbdc9c39daaaf52a4c0937b9f06975808@167.235.198.193:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
