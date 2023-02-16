# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/cosmoshub.png" width="150" alt=""><figcaption></figcaption></figure>

The Cosmos Hub is the blockchain protocol underlying an  increasingly large number of blockchains built on the  Cosmos Network, allowing them to communicate with each other.

**Chain ID**: cosmoshub-4 | **Latest Version Tag**: v8.0.0 | **Wasm**: OFF

[Website](https://hub.cosmos.network) | [Discord](https://discord.gg/cosmosnetwork) | [Twitter](https://twitter.com/cosmoshub)




## Chain explorer
[https://explorer.kjnodes.com/cosmoshub](https://explorer.kjnodes.com/cosmoshub)

## Public endpoints

* api: [https://cosmoshub.api.kjnodes.com](https://cosmoshub.api.kjnodes.com)
* rpc: [https://cosmoshub.rpc.kjnodes.com](https://cosmoshub.rpc.kjnodes.com)
* grpc: [https://cosmoshub.grpc.kjnodes.com](https://cosmoshub.grpc.kjnodes.com)

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

**live-peers** (13)
```bash
peers="1d02b4300c6b6fd1123a20502f0b3c0ce3b73654@88.198.16.9:26656,c1e437f73b8889b78ea34981e7c349157ad80284@107.135.15.66:26656,44594a57ce538a21f8558bcb1c9ce560ad879e3e@15.235.114.84:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:34656,460967e46cc013e5e3eb365c1a8d271b0662549f@35.208.242.182:26656,222385f3ce7f55f9c01c23f2ee340ed9548b18fa@35.222.169.98:26656,4c46d32cbc4777c59a91a53fdadf8a3fa362036e@116.202.10.68:26656,2633bc088bcf96209b695734005952906b5c45e3@3.123.191.80:26656,9c116194f25fd0d146019f171ef0f49904dcc586@167.86.98.230:26656,39f68cf5744a881ea73023bf4e02db36390cfb1f@146.190.59.8:26090,625fbb458b228229bcfaec6b834c1aa40f634bbf@165.22.199.234:26090,87ccc1dcc0b846fc1623ab9a5ab55682e8e2ad2e@47.147.226.228:26656,3750b5a4288071182eb591b1538320a96f7af267@65.108.69.17:26001"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gaia/config/config.toml
```
