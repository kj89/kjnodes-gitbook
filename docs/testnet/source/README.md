# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/source.png" alt=""><figcaption></figcaption></figure>

Source is a decentralized, permissionless, and censorship resistant layer 1 proof-of-stake blockchain built in the Cosmos Zone ecosystem.

**Chain ID**: sourcechain-testnet | **Latest Version Tag**: v1.0.0 | **Wasm**: ON

[Website](https://www.sourceprotocol.io) | [Discord](https://discord.io/SourceProtocol) | [Twitter](https://www.twitter.com/sourceprotocol_)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/source-testnet](https://explorer.kjnodes.com/source-testnet)

## Public endpoints

* api: [https://source-testnet.api.kjnodes.com](https://source-testnet.api.kjnodes.com)
* rpc: [https://source-testnet.rpc.kjnodes.com](https://source-testnet.rpc.kjnodes.com)
* grpc: source-testnet.grpc.kjnodes.com:12890

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@source-testnet.rpc.kjnodes.com:12856
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@source-testnet.rpc.kjnodes.com:12859
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/source-testnet/addrbook.json > $HOME/.source/config/addrbook.json
```

**live-peers** (10)
```bash
peers="cac254555deea35a70c821abd7f3e7db47a46d55@65.109.92.241:20056,5fb7f75e3a97fa0f936020b62daf1e67281f7f16@65.109.92.240:20056,db69700d8b0c277183ab1ec34d79a083c2578d32@65.21.145.209:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12856,d960215e0788fcfc04b9e2e824e5751bf1efe7fc@65.108.82.152:26656,b24ae5d099d5564a227aa7b1a8278293b8db0cfa@185.255.131.27:26656,cba9a7c35b554596577e9708d405eb83b1f2a6d2@65.21.248.172:26656,854048fcfb453297742b76cc5c6b7555eeb25110@213.239.207.175:31656,e225dac8c3407df8419fb01f4255d72212a3b6ee@194.233.80.252:26656,a833e9d068c7f5f32f411662c0430196a88aee91@65.109.65.248:28656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
