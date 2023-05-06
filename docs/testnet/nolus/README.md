# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nolus.png" alt=""><figcaption></figcaption></figure>

Nolus aims to be the leading DeFi Lease platform. The protocol  intends to become a tool for empowering people, simple to use, and highly efficient.

**Chain ID**: nolus-rila | **Latest Version Tag**: v0.3.0 | **Wasm**: ON

[Website](https://www.nolus.io) | [Discord](https://discord.gg/nolus-protocol) | [Twitter](https://twitter.com/NolusProtocol)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/nolus-testnet](https://explorer.kjnodes.com/nolus-testnet)

## Public endpoints

* api: [https://nolus-testnet.api.kjnodes.com](https://nolus-testnet.api.kjnodes.com)
* rpc: [https://nolus-testnet.rpc.kjnodes.com](https://nolus-testnet.rpc.kjnodes.com)
* grpc: nolus-testnet.grpc.kjnodes.com:14390

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nolus-testnet.rpc.kjnodes.com:14356
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nolus-testnet.rpc.kjnodes.com:14359
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nolus-testnet/addrbook.json > $HOME/.nolus/config/addrbook.json
```

**live-peers** (10)
```bash
peers="acd39ab5b00e5611df296b2e6fb4f6a44a32513f@23.88.5.169:21656,2ecc48753d6f60a5556d917086f11ea34e18914d@84.46.252.48:26656,c3eeb6117374834beaa674cb7a8769dc6ac9f672@135.181.33.188:37656,6d76e4e0f73efa4e693b9d32934b09a025c6aa62@38.242.128.166:26656,73290354a81324fca070cef5158b272925f102a2@65.109.92.235:11006,b7d04a32d5c0e9b7e1095c4d81f5bebfd03138db@65.108.8.28:61456,e367dd3cbfca4b6d78271ed5585c469d9f1cb4b4@51.89.6.150:31656,647c0cefcd470b6d92b03b3511a0a4defe2a30dd@135.181.208.169:31656,22acc593150fc38f9b1a2dc93cdc05e22566e7f6@213.239.207.165:29856,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14356"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
