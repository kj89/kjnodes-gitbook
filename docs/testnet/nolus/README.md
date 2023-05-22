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
peers="1a5f37caaa5dd174bc2797bf2a70b804e71bc632@162.55.42.27:26656,e6b3d520d342782129689d5f9aee6c8f12933a61@51.89.7.235:26649,c6e62e0d9998413692ce1aefd05ae5eeb699a691@65.109.122.105:60756,236a2626ad46bb671b200883b6105350310372ef@135.181.81.65:37656,38e75806248cd215e1e71d94e3db8c08bcf87702@95.214.55.138:27656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14356,15cd61c8528611d1192ee06578cd6f5054645a0e@46.101.115.206:55666,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,8089ad7527be4d7823afc2cbaa1f3729506190d9@185.205.246.155:26656,acd39ab5b00e5611df296b2e6fb4f6a44a32513f@23.88.5.169:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
