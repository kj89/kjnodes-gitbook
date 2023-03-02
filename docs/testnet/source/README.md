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
peers="fae907ab505bfd41fc2499bd002fd58adc6fc68a@173.249.26.69:26656,7143126daf3c0983745a0b10b83c8e794c4fb2fc@65.108.126.46:33656,db69700d8b0c277183ab1ec34d79a083c2578d32@65.21.145.209:26656,f9c66449320c103f6c33b10f5926b20732a3bd10@194.60.201.69:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,b5cfe488ddf0b9e902716b2e18686f8b13c03182@62.171.181.251:26656,9260303a16969bbf4360b462d80ce12f77c4d3a1@43.131.35.28:26656,d960215e0788fcfc04b9e2e824e5751bf1efe7fc@65.108.82.152:26656,a9e8376ba9309bdcf5d6ed00e8960d70a03bb3f2@213.202.218.28:26656,e225dac8c3407df8419fb01f4255d72212a3b6ee@194.233.80.252:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
