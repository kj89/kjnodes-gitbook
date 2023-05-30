# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/zetachain.png" alt=""><figcaption></figcaption></figure>

An EVM-compatible L1 blockchain that connects everything:  Build interoperable dApps that span any chain including Bitcoin; access all chains from one place.

**Chain ID**: athens_7001-13 | **Latest Version Tag**: latest | **Wasm**: OFF

[Website](https://www.zetachain.com) | [Discord](https://discord.gg/zetachain) | [Twitter](https://twitter.com/zetablockchain)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/zetachain-testnet](https://explorer.kjnodes.com/zetachain-testnet)

## Public endpoints

* api: [https://zetachain-testnet.api.kjnodes.com](https://zetachain-testnet.api.kjnodes.com)
* rpc: [https://zetachain-testnet.rpc.kjnodes.com](https://zetachain-testnet.rpc.kjnodes.com)
* grpc: zetachain-testnet.grpc.kjnodes.com:16090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@zetachain-testnet.rpc.kjnodes.com:16056
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@zetachain-testnet.rpc.kjnodes.com:16059
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/zetachain-testnet/addrbook.json > $HOME/.zetacored/config/addrbook.json
```

**live-peers** (27)
```bash
peers="a918d08544b5f4e0a9eb20bf91f343eb71b6d5ee@164.90.181.99:26656,24a3a8151ec9ecec0b9ed1ca97accfb1dacc115f@88.218.226.79:26656,983972c8d76558b5f0150cd6bffc10ce4f608e4c@65.21.236.163:26656,af58c82b5f4d2268e0b8ca9150190e438c07d90d@34.239.99.239:26656,038234610497601373b1d27e27251674c6c81df7@3.218.170.198:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:16056,809c1bdb33c162fdc380372523ccd58131368380@54.77.180.134:26656,af10c27ac4539b6c7f593013267d25797cf68ff2@54.187.106.246:26656,853c46d580fe0673aba2b72b4b93b9d156b882fb@52.42.64.63:26656,57693a9bce3ffb5d6023a161ac9f744ac09a2329@162.19.240.28:26656,b96c038643c08373535956e3505a5aa955fadb0a@54.254.133.239:26656,be0f264f08c66603a6edf74516f27c5bbe5fe53e@44.230.111.72:26656,dc40518d8e8fa23b48e17de4e211a07f04168e5c@54.210.102.215:26656,a6090cdf3ff4bdc428ba89c4f622ec1b3490e338@18.143.71.236:26656,66338a18a755a0c780b011f012ff142ebaa8fa56@44.236.174.26:26656,7b1e4c6dbdeb65fbaafd5fe415679d252bdae2f9@141.94.214.137:26656,bc172d609b49146ca63ea47c0f7e1f04fa4a7458@44.226.121.184:26656,fe8a706ce2538ba81429f89a1bfd28f4e39e9b7d@13.228.103.187:26656,51405784f4a8376134a68cf350c0213f0830bf51@3.211.83.113:26656,4226fcb3b3809c00bc56283063fc52fa4bfc9a17@18.210.106.52:26656,828a6e980767d83ee0d6eb798f6cadbad6446566@31.132.165.22:26756,fc5316e6ada821627224a5efa2abb9d9a9c6c8f4@52.49.116.66:26656,7581f6a7b3913b900f172633df4e555342b350b1@202.8.10.137:26656,2af8a5ff35b7bddece613f95c2af428ac0f4d062@13.213.91.81:26656,03ff657e528ab815721981e4ae5d2740fbf49df3@148.251.12.27:26656,083f16db4a20bed979e577c303fd5403d7be77b7@205.209.103.170:26656,388f5fd1396bed6d962980e0f3adf1aa02689a7a@5.161.104.23:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.zetacored/config/config.toml
```
