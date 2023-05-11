# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/haqq.png" alt=""><figcaption></figcaption></figure>

Haqq is the blockchain network that issues Islamic Coin,  its native cryptocurrency. Haqq is fast, trusted and  compatible with thousands of applications around the world.

**Chain ID**: haqq_54211-3 | **Latest Version Tag**: v1.3.1 | **Wasm**: OFF

[Website](https://islamiccoin.net) | [Discord](https://discord.gg/hU9MHG5kZq) | [Twitter](https://twitter.com/Islamic_Coin)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/haqq-testnet](https://explorer.kjnodes.com/haqq-testnet)

## Public endpoints

* api: [https://haqq-testnet.api.kjnodes.com](https://haqq-testnet.api.kjnodes.com)
* rpc: [https://haqq-testnet.rpc.kjnodes.com](https://haqq-testnet.rpc.kjnodes.com)
* grpc: haqq-testnet.grpc.kjnodes.com:13590

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@haqq-testnet.rpc.kjnodes.com:13556
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@haqq-testnet.rpc.kjnodes.com:13559
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/haqq-testnet/addrbook.json > $HOME/.haqqd/config/addrbook.json
```

**live-peers** (10)
```bash
peers="8238ddf162ce8a144610e671c63226b0207a1f73@38.242.148.96:36656,a6150d39e4725d28a56f41ebf3c6d457c54bd2f1@34.138.250.4:26656,eb503dddcc41ba801c646d63cc762de4e9c43aa4@35.228.23.164:26656,24e894d4d8a18276acf6051cccf369a1ce69842d@65.108.151.105:26656,32a8eec046b95e8646ff0810b4596dc7083a0beb@65.108.145.131:26656,f54d4de6d4ae81ec8a2315b54247872b315f198d@65.109.57.9:26656,ccff2d110a06e8a76fd1529200d96316eb077007@65.108.78.116:46656,b8a448782429ee7679c580ec5ef20a7325916cb3@202.61.194.254:56656,7f2828e3910a4b165a65e5bfb2465c1e809bad3b@65.108.48.182:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.haqqd/config/config.toml
```
