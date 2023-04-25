# Services

[installation](./installation/ "mention") [upgrade](./upgrade/ "mention") [snapshot](./snapshot/ "mention") [state-sync](./state-sync/ "mention") [useful-commands](./useful-commands/ "mention")

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/cosmoshub.png" width="150" alt=""><figcaption></figcaption></figure>

The Cosmos Hub is the blockchain protocol underlying an  increasingly large number of blockchains built on the  Cosmos Network, allowing them to communicate with each other.

**Chain ID**: cosmoshub-4 | **Latest Version Tag**: v9.0.0 | **Wasm**: OFF

[Website](https://hub.cosmos.network) | [Discord](https://discord.gg/cosmosnetwork) | [Twitter](https://twitter.com/cosmoshub)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/cosmoshub](https://explorer.kjnodes.com/cosmoshub)

## Public endpoints

* api: [https://cosmoshub.api.kjnodes.com](https://cosmoshub.api.kjnodes.com)
* rpc: [https://cosmoshub.rpc.kjnodes.com](https://cosmoshub.rpc.kjnodes.com)
* grpc: cosmoshub.grpc.kjnodes.com:34090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@cosmoshub.rpc.kjnodes.com:34656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@cosmoshub.rpc.kjnodes.com:34659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/cosmoshub/addrbook.json > $HOME/.gaia/config/addrbook.json
```

**live-peers** (30)
```bash
peers="6eade50fdbad0b600e2d1e9babbce6d2b1b99429@3.34.112.158:26656,e829d4764a5cecc44b3414777853b34407b36601@185.16.39.179:26656,47d821be546d8658b8cfb29f0d071e68228c6f0d@148.251.192.140:26656,213857e741833d17275ea559bb2d0342398cec99@35.245.206.45:26656,e3f76b923d03fc99510b31049144e22d8f0f0587@65.108.193.249:2010,c124ce0b508e8b9ed1c5b6957f362225659b5343@169.155.44.11:26656,62da9d5bc8768e84400941a1195f47bac90fcf97@35.210.106.206:26656,b6b9bc1a0c18d12be759111bb3a0d9a8958120c7@57.128.20.184:26656,e0ab6c5cc86959853f499236b8297344802ac5f4@5.161.139.201:26656,0eeb20e044d632b279e67f2fe91f50e4fceab1fd@159.223.223.84:26656,1da54d20c7339713f1d6d28dd2117087dd33d0ca@5.9.59.145:26656,ca5011c44fd74d95e7fca487c69e301df195750c@65.108.122.246:26726,f05ddce65f1e75babe01d05fef1bce5d8ffe0972@54.177.181.170:26656,ee767901f4a7eaf44603ef0a5b6e5edac118ba1e@74.118.136.149:26656,1279eae188599463661c3e2b9ab492615a6d7079@65.108.235.32:2010,e726816f42831689eab9378d5d577f1d06d25716@23.88.22.1:26656,fe21dd474640247888fc7c4dce82da8da08a8bfd@135.181.113.227:26656,0255a6594d169ea042a3a3694f279daf2eb7ab4a@103.126.158.30:26656,993d38129fcb402cb9733a0f6a9798f6d1a8f8ed@15.235.51.48:26656,1cce99042f884d669e7287e3e362bff8e385c63e@46.4.79.183:26726,2532ad5b2f93fd521e97dbc3562db711df4bd763@65.109.88.70:26656,9e14c8c48776a789f7029e88c260b2a6cbbf1417@35.212.85.141:26656,b79e1d3a621bdafd3a8d9a49dff8f4737d0bedc9@52.73.168.104:26656,803abd0b6b0478ab7f7e38dbda89902ca67f8778@65.21.90.137:11956,db7850e8e9bef0568904b7d5bcaec813e8e3d295@34.27.227.166:26656,c0e99d6797507c8ba3e97afda4400c9e9d986495@148.251.132.176:26656,ea1779f3c46730e98727fbc0499ba45b31a40ce0@95.216.16.205:14956,9edd51012df3a09395a48eb68a84723d6308e08c@35.212.116.100:26656,6f473f7156b9e0a460f5ab9d5b8bba2412058974@93.159.134.156:36656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:34656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gaia/config/config.toml
```
