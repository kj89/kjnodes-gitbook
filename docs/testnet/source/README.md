# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/source.png" width="150" alt=""><figcaption></figcaption></figure>

Source is a decentralized, permissionless, and censorship resistant layer 1 proof-of-stake blockchain built in the Cosmos Zone ecosystem.

**Chain ID**: sourcechain-testnet | **Latest Version Tag**: v1.0.0 | **Wasm**: OFF

[Website](https://www.sourceprotocol.io/) | [Discord](https://discord.io/SourceProtocol) | [Twitter](https://www.twitter.com/sourceprotocol_)




## Chain explorer
[https://explorer.kjnodes.com/source-testnet](https://explorer.kjnodes.com/source-testnet)

## Public endpoints

* api: [https://source-testnet.api.kjnodes.com](https://source-testnet.api.kjnodes.com)
* rpc: [https://source-testnet.rpc.kjnodes.com](https://source-testnet.rpc.kjnodes.com)
* grpc: [https://source-testnet.grpc.kjnodes.com](https://source-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@source-testnet.rpc.kjnodes.com:28656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@source-testnet.rpc.kjnodes.com:28659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/source-testnet/addrbook.json > $HOME/.source/config/addrbook.json
```

**live-peers** (10)
```bash
peers="1450d99427abd81410c6f8032aec25961bf7bf89@80.82.215.19:36656,4675f239ef3bd4cef7fa2770232b2eeea0008260@212.118.38.133:26656,bdf9b6ad38b803358e7fd99f35b14795ebcd8144@190.2.155.67:29656,b99c46a83e72280ccdb81994fd60b9b1cc74b1ab@84.21.171.142:26656,7143126daf3c0983745a0b10b83c8e794c4fb2fc@65.108.126.46:33656,d960215e0788fcfc04b9e2e824e5751bf1efe7fc@65.108.82.152:26656,6e4cdcb3039f1f8e97b8511c3b146cd14d41dc3d@65.109.112.20:11084,14d1da3e6798ae897a551d179f91c4c4434d633f@178.20.43.18:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,383a0684aadfe507e097c36b34d6243da59d9ed5@207.180.232.91:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
