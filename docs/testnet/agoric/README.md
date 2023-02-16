# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/agoric.png" width="150" alt=""><figcaption></figcaption></figure>

Agoric is an interoperable Proof-of-Stake chain in the Cosmos ecosystem.  Agoric JavaScript smart contract platform enables 15M+ developers across the  globe to rapidly build and deploy dapps on-chain.

**Chain ID**: agoric-emerynet-5 | **Latest Version Tag**: pismoA | **Wasm**: OFF

[Website](https://agoric.com) | [Discord](https://discord.com/invite/qDW8DRes4s) | [Twitter](https://twitter.com/agoric)




## Chain explorer
[https://explorer.kjnodes.com/agoric-testnet](https://explorer.kjnodes.com/agoric-testnet)

## Public endpoints

* api: [https://agoric-testnet.api.kjnodes.com](https://agoric-testnet.api.kjnodes.com)
* rpc: [https://agoric-testnet.rpc.kjnodes.com](https://agoric-testnet.rpc.kjnodes.com)
* grpc: [https://agoric-testnet.grpc.kjnodes.com](https://agoric-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@agoric-testnet.rpc.kjnodes.com:27656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@agoric-testnet.rpc.kjnodes.com:27659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/agoric-testnet/addrbook.json > $HOME/.agoric/config/addrbook.json
```

**live-peers** (24)
```bash
peers="a875ef614b3902dd567be2076f18239681f24e35@185.146.148.112:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.136:27106,42084028a65c5d609793ffc618d1dcbf374fc301@65.109.28.219:14456,32f7fbecd40b420d592ac460703c4ac647875566@65.109.23.238:26656,4dee5e4456307469d037c35eb0157f1f252b3f99@135.181.35.255:26656,a5b991654d0723e038d3723b1345b2a288d49146@38.242.156.28:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:27656,6f9e22eba0130f1a29c25e28beeae69b2621a403@35.226.248.0:26656,3f4e87ddb2e61fdd01398c071fa986259f096334@209.34.206.46:26656,a753081b566e32ed2b702b6e4edc3ff01f246d04@5.75.240.73:26656,a3a1e6c7a9ceec632c22769a9e369d05a796dc24@65.108.79.246:26709,fd9d8063921531990cfebb72d5adadf276484e8d@13.215.217.74:26656,7ea47a018710e43a9eafd4eebc8340d2f48eb3ba@94.130.132.227:2160,c72d05f83b53dc7f6c55d7d3e67c304716d27d80@116.202.227.117:27656,fed5712837f1561b7ac4eebbbf618df7c76104d9@51.81.185.12:44656,7b1cafa0879374125c623d854bcc0cb9cd98729e@185.213.25.151:26656,980583e1dfd16988b6fdb22dd733f3260c535e45@192.241.137.132:26656,d238a541e480e06269107449a70b1178ef49aba7@35.224.177.96:26656,793955daf95ad29f003cc4ec7e6c60c00677b2f7@5.9.81.187:30656,a350a919fc1295f441732b4264c6603983f720e5@35.238.67.135:26656,98e1069b1cfc445e377eda6a0eadd94f7877065d@162.55.169.76:26656,3c2abc308efdc63be1801bbb1b40900ada13349b@34.69.172.140:26656,8dfb920cdc2eba42b688f44fdd26e12dabfbb6a9@95.217.130.111:27656,a73444541956b994f804f6fcf2a26d2c3c9865a3@35.184.189.155:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.agoric/config/config.toml
```
