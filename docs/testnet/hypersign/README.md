# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/hypersign.png" width="150" alt=""><figcaption></figcaption></figure>

Hypersign is a decentralized identity layer for the internet, giving  users control of their personal data and identity whilst digital  enabling trust for businesses.

**Chain ID**: jagrat | **Latest Version Tag**: v0.1.6 | **Wasm**: OFF

[Website](https://hypersign.id) | [Discord](https://discord.gg/DmuUjMrHVw) | [Twitter](https://twitter.com/hypersignchain)




## Chain explorer
[https://explorer.kjnodes.com/hypersign-testnet](https://explorer.kjnodes.com/hypersign-testnet)

## Public endpoints

* api: [https://hypersign-testnet.api.kjnodes.com](https://hypersign-testnet.api.kjnodes.com)
* rpc: [https://hypersign-testnet.rpc.kjnodes.com](https://hypersign-testnet.rpc.kjnodes.com)
* grpc: [https://hypersign-testnet.grpc.kjnodes.com](https://hypersign-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@hypersign-testnet.rpc.kjnodes.com:31656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@hypersign-testnet.rpc.kjnodes.com:31659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/hypersign-testnet/addrbook.json > $HOME/.hid-node/config/addrbook.json
```

**live-peers** (10)
```bash
peers="23eff008c88dcc60ef9a71f2fb469c472679c35e@136.243.88.91:5040,7d85caec437cc8c0a504d6ab3b18fd07c173b2fb@94.130.219.37:26001,0188d0143ea4311923a809bb07ee9ebf13c0c63b@94.130.16.254:60656,1380864bb38481fef4b2358026a5ed53fc027679@95.214.52.206:26656,bd2ae9f1c42183104719f7c44be078bb7d282a61@65.109.92.241:11056,5b6356defbfc7227035698d6af7d686d3981a0eb@5.161.99.136:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:31656,d72875380d7b0b68f071623996bd5a86b7491287@116.202.227.117:31656,0c6758a3f4554bbc67da73993bbb697764c5c534@38.242.142.227:26656,efcb16ec33d8e6233d1068fff679c6fd64bf5802@65.108.225.158:10956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.hid-node/config/config.toml
```
