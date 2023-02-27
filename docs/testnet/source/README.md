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
peers="2b2f270bd3bd1d518d87ca057597348cd8582698@109.123.252.3:26656,bdf9b6ad38b803358e7fd99f35b14795ebcd8144@190.2.155.67:29656,d960215e0788fcfc04b9e2e824e5751bf1efe7fc@65.108.82.152:26656,cac254555deea35a70c821abd7f3e7db47a46d55@65.109.92.241:20056,8b75c926d4060560dbbead7d8b0300b7b411ff9b@5.252.193.133:26656,c749b47c438842d9874b515de130dfb11431360f@147.182.211.27:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:28656,7143126daf3c0983745a0b10b83c8e794c4fb2fc@65.108.126.46:33656,c11b85deb59574812a7e6b9d6181df36bef15d2f@65.108.105.48:27656,9d16b552697cdce3c8b4f23de53708533d99bc59@165.232.144.133:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
