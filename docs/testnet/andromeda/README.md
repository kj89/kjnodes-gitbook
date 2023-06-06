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

**live-peers** (10)
```bash
peers="c45d01b216a7f24a06448a47b6cf19a42e74c29b@65.21.170.3:32656,99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656,a537cc2879fc79401f6834aa6483fbb1dee18ef0@137.184.44.33:20156,32e94653d765d9a43eb9c7a97d752dd96b2a50d6@213.247.154.10:26656,6655d577238453036a063a17a214c9e81f7b6451@185.249.225.63:47656,20248068f368f5d1eda74646d2bfd1fcdaffb3e1@89.58.59.75:60656,815e9378b05a40e4a774223b55f5c6b8457a1c79@31.220.79.166:26656,62f7aaafd73816bdaf685a6270541c1d1f8162ad@155.133.27.170:26656,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
