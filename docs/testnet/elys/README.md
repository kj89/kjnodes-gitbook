# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/elys.png" width="150" alt=""><figcaption></figcaption></figure>

Elys is a fast layer 1 blockchain powered by the Cosmos-SDK.  It is the first, and only, decentralized suite of financial  applications in the Cosmos ecosystem that has built-in native  bridging capabilities for optimal user experience and value  capture, and native margin trading capabilities that are  powered by liquidity pools & liquidity providers.

**Chain ID**: elystestnet-1 | **Latest Version Tag**: v0.3.1 | **Wasm**: OFF

[Website](https://elys.network) | [Discord](https://discord.gg/R9Gr6Vh7vC) | [Twitter](https://twitter.com/elys_network)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/elys-testnet](https://explorer.kjnodes.com/elys-testnet)

## Public endpoints

* api: [https://elys-testnet.api.kjnodes.com](https://elys-testnet.api.kjnodes.com)
* rpc: [https://elys-testnet.rpc.kjnodes.com](https://elys-testnet.rpc.kjnodes.com)
* grpc: elys-testnet.grpc.kjnodes.com:53090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@elys-testnet.rpc.kjnodes.com:53656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@elys-testnet.rpc.kjnodes.com:53659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/elys-testnet/addrbook.json > $HOME/.elys/config/addrbook.json
```

**live-peers** (30)
```bash
peers="3174bb06e87392c74ad65a80c42feed816366a84@68.183.210.88:21956,501767323c5223bfe138d916189cb5427f7e3931@104.193.254.42:27656,1cd3163afca4ad48949afdf6f18133fd3181e303@65.108.40.46:57656,86fef1d45a77465c7b2a1dd168a792b7dd3c8f37@178.128.24.90:21956,5c2a752c9b1952dbed075c56c600c3a79b58c395@178.211.139.77:27296,b06c8ad5bb82d577acd0060242e225980db88377@65.108.225.70:26656,587e0c84a487b2e0782e5d9b80ded838db9512b9@78.110.161.68:26656,e92be3a72a23a0c944633e63a67d0db1587dd98a@167.71.209.28:21956,0ea4e8352215aad85ff33a20a3bf4acf49070662@64.226.117.34:21956,72830131de8c4d80cad5e69326d7dc570be4dcf8@65.109.28.226:17656,42ec80cecb5fcda3d304d10b5302d824a3aeba5a@178.128.241.104:38656,cdf9ae8529aa00e6e6703b28f3dcfdd37e07b27c@37.187.154.66:26656,3a69f577b14bb5e3829489881cc80841b785e092@116.203.129.0:26656,8723618f5dff7ac9b57472f90f2e86a2eb194e0a@71.236.119.108:25656,18842ea01d32c76aa7d1668a734ffbac231f1fe6@81.6.58.121:26656,04fe647234dc6f180783ded240ac4d023f5bfe55@170.64.174.128:21956,0c9b0a1bc1ce796c3d9497c7400977fc5bf01379@66.94.101.52:26656,3f30f68cb08e4dae5dd76c5ce77e6e1a15084346@212.95.51.215:56656,147683d8ae2c34281fc73d6a9f6cedd5f28a15ed@185.216.203.176:21956,f29fe386022c463b3945955efe2b753e3bcad9a9@45.151.122.202:26656,e4b07652c318b08357e5796431982169789ce2c5@159.65.32.10:21956,3dd9e0f4f106cba1fa12c74927dd9b2ff80d80ef@65.108.200.60:32656,a82ae55cc1d96af39977175624537c17f6a70995@137.184.184.159:21956,ab4068efcb0e1401ff1b08f9269fa88151a640c0@154.12.229.78:26656,78aa6b222ae1f619bef03a9d98cb958dfcccc3a8@46.4.5.45:22056,79416b9dc2114b8246bf73aab6540bc55669a533@154.53.57.227:26656,1092d9a9508053d6936661ebc5708d0d8d360e3e@193.26.159.34:10656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:53656,734a87b41a015faf59a7d6266deea190421476c2@95.217.160.243:26656,45e30968d5a122a5d8e8e8c36635e6efec112839@45.151.123.12:21956"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.elys/config/config.toml
```
