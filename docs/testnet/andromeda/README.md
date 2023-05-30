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

**live-peers** (9)
```bash
peers="39308d079906ea8aadb58c552d0fe861272d11ff@38.242.196.157:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14756,a537cc2879fc79401f6834aa6483fbb1dee18ef0@137.184.44.33:20156,95e8225c5b8a21c1fecd411f37c75f5515de1891@185.197.251.203:26656,d0ef5f5583ff0343ea41962f68010bff54caafde@212.90.121.45:30656,c06d5254e4ecb69ccae41feff4d75de2dd92154d@149.102.138.176:26656,e61f287d51edab6f6dbe00a8b804614443ee6f82@80.85.242.117:26656,6ef441d08cdb54b9f058884509ec65349976d73d@178.172.212.167:26656,b6dd58949a8b9c03349bdbec8aeeccd5e0d39283@31.220.74.50:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
