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

**live-peers** (11)
```bash
peers="cba9a7c35b554596577e9708d405eb83b1f2a6d2@65.21.248.172:26656,e6a5db345775973982e32b24ba7f3bfa18337f66@65.108.124.219:33656,8b75c926d4060560dbbead7d8b0300b7b411ff9b@5.252.193.133:26656,596112703a361a71e0c3dbf1b1b04f87e1c23e47@85.239.230.135:26656,3e16844d041df0f4b14d0d624fc94eadf50ed61d@65.108.13.154:28656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12856,2b2f270bd3bd1d518d87ca057597348cd8582698@109.123.252.3:26656,148afdfb995b3aa727727a49c23324a804410a90@95.216.7.169:46656,d960215e0788fcfc04b9e2e824e5751bf1efe7fc@65.108.82.152:26656,e225dac8c3407df8419fb01f4255d72212a3b6ee@194.233.80.252:26656,6aba831746663a3f1b4fbeb30f836ef442ec02da@46.17.250.108:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
