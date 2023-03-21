# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/andromeda.png" width="150" alt=""><figcaption></figcaption></figure>

Andromeda is an application platform layer that connects all  public blockchains in the Cosmos ecosystem. Through our vast  library of no-code smart contracts, users can harness the power of web3.

**Chain ID**: galileo-3 | **Latest Version Tag**: galileo-3-v1.1.0-beta1 | **Wasm**: ON

[Website](https://www.andromedaprotocol.io) | [Discord](https://discord.gg/wzM3kSN3sE) | [Twitter](https://twitter.com/andromedaprot)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/andromeda-testnet](https://explorer.kjnodes.com/andromeda-testnet)

## Public endpoints

* api: [https://andromeda-testnet.api.kjnodes.com](https://andromeda-testnet.api.kjnodes.com)
* rpc: [https://andromeda-testnet.rpc.kjnodes.com](https://andromeda-testnet.rpc.kjnodes.com)
* grpc: andromeda-testnet.grpc.kjnodes.com:47090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@andromeda-testnet.rpc.kjnodes.com:47656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@andromeda-testnet.rpc.kjnodes.com:47659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/andromeda-testnet/addrbook.json > $HOME/.andromedad/config/addrbook.json
```

**live-peers** (15)
```bash
peers="6006190d5a3a9686bbcce26abc79c7f3f868f43a@37.252.184.230:26656,4cd929e58c35970289659e402a582115671baaee@65.109.106.91:25656,e2efe3e1d7e0ed2e5b6a1b384c47f745e9f205ac@65.108.141.109:31656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,f1d30c5f2d5882823317718eb4455f87ae846d0a@85.239.235.235:30656,99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656,3969b8ddc6d0ed9f2deb0265e4b26e88c5cb894a@149.102.150.250:30656,72bba2142c9cada7e4b8e861fb79e8a66e345d99@95.217.236.79:50656,0cc98f28ed826b3b43d2c88deb214ff01b36f6ce@159.69.126.18:15656,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,20248068f368f5d1eda74646d2bfd1fcdaffb3e1@89.58.59.75:60656,3d25f45062b5f3f49a87d38300ca0f657a9c853f@84.252.159.238:02656,a14e423bd01f55bdc29c2eeac99aaa0398e94228@45.14.194.212:26656,1c101b595362f6a5856ef34f43545cf95eb34912@65.109.26.21:15656,8870aca1936673bb2068ed07fcadc6c46d3ec3a1@146.190.83.6:22656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
