# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/ollo.png" alt=""><figcaption></figcaption></figure>

OLLO is a sovereign L1 chain built on the Cosmos network providing  next-gen trading tools & sustainable tokenomics.

**Chain ID**: ollo-testnet-1 | **Latest Version Tag**: v0.0.1 | **Wasm**: OFF

[Website](https://www.ollostation.zone) | [Discord](https://discord.com/invite/GxBqZ9mSSm) | [Twitter](https://twitter.com/OLLOStation)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/ollo-testnet](https://explorer.kjnodes.com/ollo-testnet)

## Public endpoints

* api: [https://ollo-testnet.api.kjnodes.com](https://ollo-testnet.api.kjnodes.com)
* rpc: [https://ollo-testnet.rpc.kjnodes.com](https://ollo-testnet.rpc.kjnodes.com)
* grpc: ollo-testnet.grpc.kjnodes.com:13290

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@ollo-testnet.rpc.kjnodes.com:13256
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@ollo-testnet.rpc.kjnodes.com:13259
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/ollo-testnet/addrbook.json > $HOME/.ollo/config/addrbook.json
```

**live-peers** (10)
```bash
peers="bc73e1f3bde267171309e723416690c9c7404881@142.132.199.236:27656,dd577d8f2e997d7e70495640aff124ddb70d1a21@95.217.192.222:26656,d14b740968d24aa5c31ade7dbda2b1204c40f24c@65.109.52.156:46656,9865c6e15faced6643adc228e3a59744e1b4e277@116.203.29.162:46656,3ea40f63890f10272201edf96d2a49e197e52091@65.108.105.48:18156,7864a2e4b42e5af76a83a8b644b9172fa1e40fa5@52.8.174.235:26656,ab89596768849d679ed11a9e1848224760a278cc@83.171.248.175:32656,dba5e8b41c4e369418f83a449966e4eb7ca05cd4@65.109.23.114:18156,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13256,e2d59891f1aed38fe8884c63e0bb00f8ddc41b6f@5.78.46.66:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ollo/config/config.toml
```
