# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/andromeda.png" alt=""><figcaption></figcaption></figure>

Andromeda is an application platform layer that connects all  public blockchains in the Cosmos ecosystem. Through our vast  library of no-code smart contracts, users can harness the power of web3.

**Chain ID**: galileo-3 | **Latest Version Tag**: galileo-3-v1.1.0-beta1 | **Wasm**: ON

[Website](https://www.andromedaprotocol.io) | [Discord](https://discord.gg/wzM3kSN3sE) | [Twitter](https://twitter.com/andromedaprot)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/andromeda-testnet](https://explorer.kjnodes.com/andromeda-testnet)

## Public endpoints

* api: [https://andromeda-testnet.api.kjnodes.com](https://andromeda-testnet.api.kjnodes.com)
* rpc: [https://andromeda-testnet.rpc.kjnodes.com](https://andromeda-testnet.rpc.kjnodes.com)
* grpc: andromeda-testnet.grpc.kjnodes.com:14790

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@andromeda-testnet.rpc.kjnodes.com:14756
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@andromeda-testnet.rpc.kjnodes.com:14759
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/andromeda-testnet/addrbook.json > $HOME/.andromedad/config/addrbook.json
```

**live-peers** (11)
```bash
peers="debdccc98a2f6ed72561d7866381003903197935@144.126.142.78:29656,a537cc2879fc79401f6834aa6483fbb1dee18ef0@137.184.44.33:20156,6006190d5a3a9686bbcce26abc79c7f3f868f43a@37.252.184.230:26656,8a551bc0cc7ba190db9126c8fc95c8b643ae511c@195.201.174.109:56656,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,0f966c78a7ac4722bd389f5c010efb8235ca8f73@65.108.227.112:14656,8083dd301a7189284bf5b8d40c4cf239360d653a@5.9.122.49:26656,91fde61878d704917f882694b271b67a38865ddc@149.102.142.94:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14756,3d25f45062b5f3f49a87d38300ca0f657a9c853f@84.252.159.238:02656,c45d01b216a7f24a06448a47b6cf19a42e74c29b@65.21.170.3:32656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
