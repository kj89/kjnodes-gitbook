# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/humans.png" alt=""><figcaption></figcaption></figure>

Humans is Blockchain of AIs. It is the first blockchain network  from the Cosmos ecosystem capable of managing, deploying and  executing artificial intelligence on the blockchain.

**Chain ID**: humans_3000-31 | **Latest Version Tag**: v0.2.2 | **Wasm**: OFF

[Website](https://humans.ai) | [Discord](https://discord.gg/humansdotai) | [Twitter](https://twitter.com/humansdotai)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/humans-testnet](https://explorer.kjnodes.com/humans-testnet)

## Public endpoints

* api: [https://humans-testnet.api.kjnodes.com](https://humans-testnet.api.kjnodes.com)
* rpc: [https://humans-testnet.rpc.kjnodes.com](https://humans-testnet.rpc.kjnodes.com)
* grpc: humans-testnet.grpc.kjnodes.com:12290

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@humans-testnet.rpc.kjnodes.com:12256
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@humans-testnet.rpc.kjnodes.com:12259
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/humans-testnet/addrbook.json > $HOME/.humansd/config/addrbook.json
```

**live-peers** (11)
```bash
peers="b9767aa2312748caaf67425890768d85186b69b1@5.9.87.205:26646,946b549550e9c564193bf4c963d84b17e5415a50@136.243.136.241:26656,59ad24780f3d8b90da29079a8a386aa1355969ef@144.76.45.59:26656,a7eaa41b5565295810b81641e0bf11a9fb2ca54e@159.69.69.183:26656,6271d80b8fc42da3a2825cc5ef75818dd52423d1@138.201.121.185:26656,3563bf0924f203b6b7c5e31c21c1de4a8f2e0949@178.23.126.92:26656,e1c43f090cef72f675c37f97ed2117417e251823@65.109.92.240:1166,ad61f83dc506e821c08df82e8db4d170322e928c@5.161.64.185:26656,5c76f2a8ecad56dc081be10dc9a3927df18add20@118.193.37.229:26656,28aab35e28e06497a7f8fc1a7a50982557bf3b2d@78.46.64.59:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.humansd/config/config.toml
```
