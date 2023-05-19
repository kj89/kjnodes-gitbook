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
peers="291a397d001fca8cf2991dfce8bc6f724d44295c@75.119.132.25:29656,e6a5db345775973982e32b24ba7f3bfa18337f66@65.108.124.219:33656,596112703a361a71e0c3dbf1b1b04f87e1c23e47@85.239.230.135:26656,756368e62cbff16f8d0edcc4d169a090464bed53@38.242.194.233:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12856,5f94cf456803179361c44c213fbc95f4da1bc3af@38.242.146.255:26656,805c327443d9a2b425d16a402c23cb9cbfa36388@178.18.243.46:26656,148afdfb995b3aa727727a49c23324a804410a90@95.216.7.169:46656,a9e8376ba9309bdcf5d6ed00e8960d70a03bb3f2@213.202.218.28:26656,3e16844d041df0f4b14d0d624fc94eadf50ed61d@65.108.13.154:28656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.source/config/config.toml
```
