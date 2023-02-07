# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/bitcanna.png" width="150" alt=""><figcaption></figcaption></figure>

BitCanna is a proof-of-stake (POS) decentralized payment network designed exclusively to serve the cannabis industry. 

**Chain ID**: bitcanna-1 | **Latest Version Tag**: v1.5.3 | **Wasm**: OFF

[Website](https://www.bitcanna.io) | [Discord](https://discord.gg/9AVrzaVQvs) | [Twitter](https://twitter.com/BitCannaGlobal)




## Chain explorer
[https://explorer.kjnodes.com/bitcanna](https://explorer.kjnodes.com/bitcanna)

## Public endpoints

* api: [https://bitcanna.api.kjnodes.com](https://bitcanna.api.kjnodes.com)
* rpc: [https://bitcanna.rpc.kjnodes.com](https://bitcanna.rpc.kjnodes.com)
* grpc: [https://bitcanna.grpc.kjnodes.com](https://bitcanna.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@bitcanna.rpc.kjnodes.com:42656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@bitcanna.rpc.kjnodes.com:42659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/bitcanna/addrbook.json > $HOME/.bcna/config/addrbook.json
```

**live-peers** (10)
```bash
peers="1b01a388eaba8f15634c1e5cd5bb7c55810250d2@135.181.219.115:27656,dd4d3c0de38aa0575436c34c237b33bc0dda3ef2@142.132.158.93:13056,d3796f3f2a179afab1485a672ace3d909cd0eeed@185.137.122.214:26656,a1ceb81a5498642753f8600a5c3b9ca056af3051@67.222.144.195:16656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:42656,97e4468ac589eac505a800411c635b14511a61bb@144.76.239.25:26656,c6658742ae4c889ecf8dee95ca2a8e4b45d46dfd@85.214.208.127:26656,5af4f132d1c63cbe9d828d58522fdbb4bd508880@136.244.29.116:31656,3635058fcdbe97e72d191faedfe4c6acab835877@107.181.235.66:16656,d7322625044ad733bce4178dc397b2b9b5f68b41@43.153.27.130:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```
