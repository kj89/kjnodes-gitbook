# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/defund.png" width="150" alt=""><figcaption></figcaption></figure>

DeFund is an L1 blockchain built for building decentralized permissionless,  on-chain trading strategies that are packaged into a dETF (decentralized  exchange-traded fund) token, tradable within any ecosystem or CEX.

**Chain ID**: defund-private-3 | **Latest Version Tag**: v0.2.1 | **Wasm**: OFF

[Website](https://www.defund.app) | [Discord](https://discord.gg/FV26pRPZ3P) | [Twitter](https://twitter.com/defund_finance)


## Public endpoints

* rpc: [https://defund-testnet.rpc.kjnodes.com](https://defund-testnet.rpc.kjnodes.com)
* api: [https://defund-testnet.api.kjnodes.com](https://defund-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@defund-testnet.rpc.kjnodes.com:40656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@defund-testnet.rpc.kjnodes.com:40659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/defund-testnet/addrbook.json > $HOME/.defund/config/addrbook.json
```

**live-peers** (19)
```
peers="c94423f1f435b7e12d05c2d59ed3a0373833d3c3@157.90.253.129:26656,e199e4d17120559bc34357d72f6595cbcd4d5cd4@173.212.216.232:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,c640df433e42f07b2d2ea11679c35a69174f6ef2@194.180.176.124:26656,d7c675fa2eef507d4e2270c442383a886cade959@207.180.248.230:26656,0a1fcc2907e50b46f021389049c79f7d124f9946@77.51.200.79:36656,6854d36513081c77a24987ab66a436e29e3e5cfa@65.21.131.215:26576,b9db73c9cac1676cd389711a18a4a64eb6ce3614@135.125.153.176:26656,9dd945f369a7aa1946e007d9547b364e69da7db8@185.192.96.140:26656,34caa18dc803a7c1c5da380f85f18bbf6e2e6126@162.55.33.123:26656,4135c03053c6f02e4ca773bee42d5c7f62922566@185.217.125.238:26656,fd3f439c775df4a7c1ced33d613124acee4187a6@194.163.154.129:40656,aee64a0d9b4f06f9f0949650fa22494b1cee1d58@84.46.244.228:26656,f4869f02f970f222d81718a7a2fcf9b3c7b1b10c@109.123.249.189:26656,d368e8fc76143f89e53f0997fd5dfef32129168c@109.110.63.204:26656,d3b7991e387ebfe26965fe4361bc0f27789b0aa4@38.242.153.15:40656,95d487c4f51295c4cd799cc7fe53d23ea7298bdf@206.246.71.251:46656,d31d9801e7a021d287570b94ffcf27b91b0d9b66@217.76.55.74:26656,c734239cb2a4a59e69de4fc52a9c4aca57285391@199.175.98.107:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
