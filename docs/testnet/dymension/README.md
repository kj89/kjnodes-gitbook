# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/dymension.png" width="150" alt=""><figcaption></figcaption></figure>

Dymension is a network of modular blockchains called RollApps  and at the center of it all is the Dymension Hub. Dymension  allows anyone to build and deploy their own consensus-free blockchain, a RollApp.

**Chain ID**: 35-C | **Latest Version Tag**: v0.2.0-beta | **Wasm**: OFF

[Website](https://dymension.xyz/) | [Discord](https://discord.gg/dymension) | [Twitter](https://twitter.com/dymensionXYZ)




## Chain explorer
[https://explorer.kjnodes.com/dymension-testnet](https://explorer.kjnodes.com/dymension-testnet)

## Public endpoints

* api: [https://dymension-testnet.api.kjnodes.com](https://dymension-testnet.api.kjnodes.com)
* rpc: [https://dymension-testnet.rpc.kjnodes.com](https://dymension-testnet.rpc.kjnodes.com)
* grpc: [https://dymension-testnet.grpc.kjnodes.com](https://dymension-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@dymension-testnet.rpc.kjnodes.com:46656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@dymension-testnet.rpc.kjnodes.com:46659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/dymension-testnet/addrbook.json > $HOME/.dymension/config/addrbook.json
```

**live-peers** (20)
```bash
peers="55f233c7c4bea21a47d266921ca5fce657f3adf7@168.119.240.200:26656,6ee2e6550cd3510c0fc912bf0632a894148a79a7@38.242.202.174:31656,a85420b25181bdb9b3a38741c48dafd5fb3b922f@209.34.206.42:26656,747d05bfe9f3e0c2e0462ac351c577699e1d9b8c@207.244.244.194:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:46656,965694b051742c2da0ea66502dd9bfeea38de265@198.244.228.235:26656,6b00d8b9ad49cc2aa8d76416613bbbb10e6f56f7@65.109.108.150:26656,36a242b6f2d779aeea4811e4e4c635a55d5274f1@45.151.123.72:26656,6204710a0d089566b6df85ae4aee595afdd23cbb@146.190.40.115:26656,6c0ddab56755cd010f65f1f1201d29120a2d9092@38.242.202.200:31656,b8d08951d68da03af8f9272bf77684811197c289@95.216.41.160:26656,63d971a42e323f9411ef702d1f268f9862781c1f@194.163.165.176:40656,1f9bca661f7f9e2048f78107409e70d9ff4616f0@185.146.148.109:26656,7fc44e2651006fb2ddb4a56132e738da2845715f@65.108.6.45:61256,0d30a0790a216d01c9759ab48192d9154381e6c0@136.243.88.91:3240,147a0021cff3c34251adb3ad7194574011fa3192@176.57.189.36:11656,8f84d324a2d266e612d06db4a793b0d001ee62a0@38.146.3.200:20556,39794289e20cf80eba0a720eed58e7097e5686c1@136.243.103.53:46656,8d5eac1042bac34cddd25d7601789fc03cb3f3a9@168.119.213.113:46656,adf394846dc942b1fd03f6e310eda60b5eda7848@195.201.197.4:32656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
